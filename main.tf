provider "hcloud" {
  token = var.hcloud_token
}

resource "hcloud_server" "discord-guild-updates" {
  name  = "discord-guild-updates"
  image = "ubuntu-20.04"
  server_type  = "cx11"
  datacenter = "nbg1-dc3"

  lifecycle {
    create_before_destroy = true
  }
}

output "server_ip" {
  value       = "hcloud_server.discord-guild-updates.ipv4_address"
}
