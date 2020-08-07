import gym
import pybullet_envs  # noqa: F401

env = gym.make("HumanoidBulletEnv-v0")
env.render(mode="human")

env.reset()

for i in range(10000):
    env.render(mode="human")
    env.step(env.action_space.sample())
