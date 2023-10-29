terraform {
  backend "http" {
    address = "https://github.com/LukeR97/dgub-tfstate.git"
    lock_address = "https://github.com/LukeR97/dgub-tfstate.git/lock"
    unlock_address = "https://github.com/LukeR97/dgub-tfstate.git/unlock"
    username = "test"
    password = "test"
  }
}

provider "hcloud" {
  token = var.hcloud_token
}

resource "hcloud_server" "discord-guild-updates" {
  name  = "discord-guild-updates"
  image = "ubuntu-20.04"
  server_type  = "cx11"
  datacenter = "nbg1-dc3"
  ssh_keys = ["default"]
}

output "server_ip" {
  value = hcloud_server.discord-guild-updates.ipv4_address
}
