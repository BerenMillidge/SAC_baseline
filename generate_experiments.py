import os
import sys
generated_name = str(sys.argv[1])
results_save_base = str(sys.argv[2])
save_path = str(sys.argv[3])
env_names = ["SparseMountainCar","CartPoleContinuousBulletEnv-v0","InvertedPendulumSwingupBulletEnv-v0","ReacherBulletEnv-v0","PusherBulletEnv-v0","ThrowerBulletEnv-v0","HalfCheetahBulletEnv-v0","StrikerBulletEnv-v0","AntBulletEnv-v0","HopperBulletEnv-v0","HumanoidBulletEnv-v0"]
env_save_names = ["mountain_car","cartpole","inverted_pendulum","reacher","pusher","thrower","half_cheetah","striker","ant","hopper","humanoid"]
#base_call = (f"python main.py --env_name {env_name} --env_std 0.0 --action_repeat 3 --expl_scale 0.1 --save_every 10 --plan_horizon 30 --action_noise 0.0 --max_episode_len 500")
output_file = open(generated_name, "w")
seeds= 5
for (env_name, env_save_name) in zip(env_names, env_save_names):
    for s in range(seeds):
        log_path = results_save_base + "_"+ env_save_name + "_" + str(s)
        spath = save_path + "_" + env_save_name + "_" + str(s)
        call = (f"python main.py --env_name {env_name} --logdir {log_path} --save_path {spath}")
        print(call, file=output_file)

print("Experiment file genereated")
output_file.close()
