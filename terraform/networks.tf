resource "docker_network" "public" {
  name   = "prodstack-public-tf"
  driver = "bridge"

  ipam_config {
    subnet  = "10.0.3.0/24"
    gateway = "10.0.3.1"
  }
}

resource "docker_network" "private" {
  name     = "prodstack-private-tf"
  driver   = "bridge"
  internal = true

  ipam_config {
    subnet  = "10.0.4.0/24"
    gateway = "10.0.4.1"
  }
}
