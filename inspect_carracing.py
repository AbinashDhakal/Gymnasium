import gymnasium as gym

env = gym.make('CarRacing-v3')
print('action_space=', env.action_space)
print('observation_space=', env.observation_space)
print('action_sample=', env.action_space.sample())
env.close()
