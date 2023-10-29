terraform{
  backend "local" {
    path = "/etc"
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
