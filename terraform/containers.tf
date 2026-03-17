resource "docker_image" "app" {
  name = "prodstack-app:3.0.0"
}

resource "docker_container" "app" {
  count = 1
  name  = "tf-app"
  image = docker_image.app.image_id

  networks_advanced {
    name = docker_network.private.name
  }

  env = [
    "APP_VERSION=3.0.0"
  ]

  read_only = true

  tmpfs = {
    "/tmp" = ""
  }

  capabilities {
    drop = ["ALL"]
  }

  restart = "unless-stopped"
}
