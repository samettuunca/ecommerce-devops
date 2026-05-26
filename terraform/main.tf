terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "ecommerce" {
  name     = "ecommerce-rg"
  location = "West Europe"
}

resource "azurerm_kubernetes_cluster" "ecommerce" {
  name                = "ecommerce-aks"
  location            = azurerm_resource_group.ecommerce.location
  resource_group_name = azurerm_resource_group.ecommerce.name
  dns_prefix          = "ecommerce"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size = "Standard_D2s_v3"
  }

  identity {
    type = "SystemAssigned"
  }
}