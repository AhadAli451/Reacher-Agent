from crewai.flow import Flow, start, listen
from multiple_agents1.crews.dev_crew.dev_crew import DevCrew


class DevFlow(Flow):
    
    @start()
    def run_dev_crew(self):
        output = DevCrew().crew().kickoff(
            inputs={
                "topic":"Ai Agents. "
            }
        )
        # print("code generate", output.raw)
        # self.state.dev = output.raw
        return output.raw

def kickoff():
    dev_flow = DevFlow()
    result = dev_flow.kickoff()
    print(result)


