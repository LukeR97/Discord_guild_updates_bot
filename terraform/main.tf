provider "hcloud" {
    token = var.hetzner_token
}

resource "hcloud_server" "my_server" {
    name = "discord_guild_updates"
    image = "ubuntu-22.04"
    server_type = "cx11"
    datacenter = "nbg1-dc3"
}

