output "private_network_name" {
  value = docker_network.private.name
}

output "public_network_name" {
  value = docker_network.public.name
}

output "container_name" {
  value = docker_container.app[0].name
}
