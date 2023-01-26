from .subdomain import Subdomain
from drecon.db import db
from queue import Queue
import sys

class FlowHandler(object):

    def __init__(self,flow,domain,ts):
        self.flow=flow
        self.domain=domain
        self.subdomain=Subdomain(self.domain)
        self.flow_queue=Queue()
        self.table=db.DB(table=ts)



    def check_flow(self):

        if self.flow == "subdomain":
            self.flow_queue.put("subdomain")

        if self.flow == "subzy":
            self.flow_queue.put("subdomain")
            self.flow_queue.put("subzy")

        if self.flow == "nuclei":
            self.flow_queue.put("subdomain")
            self.flow_queue.put("nuclei")

        if self.flow == "portscan":
            self.flow_queue.put("subdomain")
            self.flow_queue.put("portscan")
        else:
            pass
        return self.run_flow()


    def run_flow(self):
        while not self.flow_queue.empty():
            flow=self.flow_queue.get()
            if flow == "subdomain":
               domains,urls=self.subdomain.run()
               self.table.insert({flow:domains})
               self.table.insert({"urls":urls})
               return domains,urls












