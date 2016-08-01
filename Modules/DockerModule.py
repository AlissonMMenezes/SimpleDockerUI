#!/usr/bin/python

from docker import Client

class DockerModule:
    def __init__(self):
        try:
            self.client = Client("tcp://127.0.0.1:2376")
            print "Conectou!"
        except Exception as e:
            print "Falhou ao conectar no docker: ",e

    def list_containers(self):
        containers = self.client.containers(all=True)
        return containers

    def stop_container(self,id):
        res = self.client.stop(container=id)
        print res
        return res

    def start_container(self,id):
        res = self.client.start(container=id)
        return res

    def create_container(self,**kwargs):
        ports = kwargs.get("port").split(":")
        print ports
        host_config = self.client.create_host_config(port_bindings={ports[1]:ports[0]})
        print host_config
        res = self.client.create_container(name=kwargs.get("name"),
                                           image=kwargs.get("image"),
                                           command=kwargs.get("command"),
                                           ports=[ports[1]],
                                           host_config=host_config,
                                           stdin_open=True,
                                           detach=True,
                                           tty=True)
        return res


    def execute_command(self,id,cmd):
        res = self.client.exec_create(container=id,cmd=cmd)
        res = self.client.exec_start(res)
        return res

    def delete_container(self,container):
        res = self.stop_container(container)
        res = self.client.remove_container(container=container)
        return "Container removed successful!!!"
