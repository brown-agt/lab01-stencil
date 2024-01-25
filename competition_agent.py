from agt_server.agents.base_agents.chicken_agent import ChickenAgent
from agt_server.local_games.chicken_arena import ChickenArena
class CompetitionAgent(ChickenAgent):
    def setup(self):
        self.SWERVE, self.CONTINUE = 0, 1
        self.actions = [self.SWERVE, self.CONTINUE]

    def get_action(self):
        # TODO: Fill out get action 
        return self.CONTINUE

    def update(self):
        return None

if __name__ == "__main__":
    #### PLEASE EDIT THESE VARIABLES #####
    agent_name = "Competition Agent"  # TODO: Please give your agent a name
    ip = '10.38.61.67' # TODO: Please ask your Lab TA for the IP of the server
    port = 8080 # TODO: Please ask your Lab TA for the correct port
    join_server = True # TODO: Set this to true if you want to join the server rather than run a local game against yourself
    
    agent = CompetitionAgent(agent_name)
    if join_server:
        agent.connect(ip=ip, port=port)
    else:
        arena = ChickenArena(
            num_rounds=1000,
            timeout=1,
            players=[
                agent,
                CompetitionAgent("Agent_1"),
                CompetitionAgent("Agent_2"),
                CompetitionAgent("Agent_3"),
                CompetitionAgent("Agent_4")
            ]
        )
        arena.run()
