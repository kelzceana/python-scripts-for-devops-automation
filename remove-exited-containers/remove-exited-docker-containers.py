import docker
client = docker.from_env()

containers = client.containers.list(all=True)

for container in containers:
   if container.status == "exited":
       print(f'Removing container {container.id} - {container.name}')
       container.remove(force=True)
   else:
       print(f'Skipping container {container.id} - {container.name}')

