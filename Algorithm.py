import numpy as np
#import matplotlib.pyplot as plt
#%matplotlib inline

#def plot_history(history):
#  rewards = history["rewards"]
#  cum_rewards = history["cum_rewards"]
#  chosen_arms = history["arms"]

#  fig = plt.figure(figsize=[30,8])

#  ax2 = fig.add_subplot(121)
#  ax2.plot(cum_rewards, label="avg rewards")
#  ax2.set_title("Cummulative Rewards")

#  ax3 = fig.add_subplot(122)
#  ax3.bar([i for i in range(len(chosen_arms))], chosen_arms, label="chosen arms")
#  ax3.set_title("Chosen Actions")

class Env(object):

  def __init__(self, reward_probas, rewards):
    if len(reward_probas) != len(rewards):
      raise Exception(f"size of reward probas : {len(reward_probas)} does not match size of rewards: {len(rewards)}")

    self.reward_probas = reward_probas
    self.rewards = rewards
    self.k_arms = len(rewards)

  def choose_arm(self, arm):
    if arm < 0 or arm > self.k_arms:
      raise Exception(f"arm must be a value between 0 and {self.k_arms -1}")

    return self.rewards[arm] if np.random.random() < self.reward_probas[arm] else 0.0

environment = Env(reward_probas=[0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06], rewards=[1200,350,250,300,600,400,250,900,400,200,280,300,200,550,300,200])
print(f"Reward Probas\t\t: {environment.reward_probas}")
print(f"Rewards \t\t: {environment.rewards}")

[environment.choose_arm(0) for _ in range(10)]

class RandomAgent(object):

  def __init__(self, env, max_iterations=2000):
    self.env = env
    self.iterations = max_iterations

  def act(self):
    arm_counts = np.zeros(self.env.k_arms)
    rewards = []
    cum_rewards = []

    for i in range(1, self.iterations + 1):
      arm = np.random.choice(self.env.k_arms)
      reward = self.env.choose_arm(arm)

      arm_counts[arm] += 1
      rewards.append(reward)
      cum_rewards.append(sum(rewards)/ len(rewards))

    return {"arms": arm_counts, "rewards": rewards, "cum_rewards": cum_rewards}

random_agent = RandomAgent(env=environment, max_iterations=2000)
ra_history = random_agent.act()
print(f"TOTAL REWARD : {sum(ra_history['rewards'])}")
print(f"Arms : {sum(ra_history['arms'])}")
print(f"Cummulative Rewards : {sum(ra_history['cum_rewards'])}")

#plot_history(eg_history)