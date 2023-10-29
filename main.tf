provider "hcloud" {
  token = var.hcloud_token
}

resource "hcloud_server" "discord-guild-updates" {
  name  = "discord-guild-updates"
  image = "ubuntu-20.04"
  server_type  = "cx11"
  datacenter = "nbg1-dc3"
  ssh_keys = [hcloud_ssh_key.default.id]

  lifecycle {
    create_before_destroy = true
  }
}

resource "hcloud_ssh_key" "default" {
  name = "default"
}

output "server_ip" {
  value = hcloud_server.discord-guild-updates.ipv4_address
}
