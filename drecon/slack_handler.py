import slack
from .flows.flow_handler import FlowHandler
from .utils import *
from app import env

class SlackHandler(object):

    def __init__(self,event):
        self.event=event
        self.user_id=self.event.get("user")
        self.channel=self.event.get("channel")
        self.ts=self.event.get("ts")

        #Slack Client
        self.client=slack.WebClient(token=env.get("SLACK_TOKEN"))


    def parse_event(self):

        if self.event.get("type") == "app_mention":

            flow,domain = filter_text(self.event.get("text"))
            self.flowHanlder = FlowHandler(flow=flow,domain=domain,ts=self.ts)
            self.domains,self.urls=self.flowHanlder.check_flow()
            self.send_msg()



    def template(self):
        pass


    def send_msg(self):
        with open("domains.txt","a") as f:
            for ele in self.domains:
                f.write(ele+"\n")
            f.close()
        with open("urls.txt","a") as f:
            for ele in self.urls:
                f.write(ele+"\n")
            f.close()


       # self.client.chat_postMessage(channel=self.channel,thread_ts=self.ts,text=self.blcok)
        self.client.files_upload(channels=self.channel,thread_ts=self.ts,file="urls.txt",filename="urls.txt")
        self.client.files_upload(channels=self.channel, thread_ts=self.ts, file="domains.txt", filename="domains.txt")








