import subprocess
import os
from app import env
from urllib.parse import urlparse
from drecon.db import db


class Subdomain(object):

    def __init__(self,domain):
        self.domain=domain
        self.httpx=["httpx","--silent"]
        self.domains=list()
        self.urls=list()

    def assetfinder(self):
        cmd = ["assetfinder","--subs-only",self.domain]
        print("executing")

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        alive = subprocess.run(self.httpx, stdin=p.stdout, stdout=subprocess.PIPE)
        for ele in alive.stdout.decode("utf-8").splitlines():
            self.urls.append(ele)

    def subfinder(self):
        print("started chaos")
        cmd = "subfinder -d {} -silent".format(self.domain).split()
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        alive = subprocess.run(self.httpx, stdin=p.stdout, stdout=subprocess.PIPE)
        for ele in alive.stdout.decode("utf-8").splitlines():
            self.urls.append(ele)

    def populate_results(self):
        for ele in list(set(self.urls)):
            self.domains.append(urlparse(ele).netloc)
        self.urls=list(set(self.urls))
        return self.domains,self.urls






    def run(self):
        self.assetfinder()
        self.subfinder()
        return self.populate_results()




