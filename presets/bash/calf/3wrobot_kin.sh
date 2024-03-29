python run_stable.py \
+seed=range\(10\) \
scenario=calf \
scenario.N_iterations=30 \
system=3wrobot_kin \
scenario.critic_model.quad_matrix_type=full \
--experiment=calf_3wrobot_kin \
+scenario.critic_safe_decay_param=1 \
+scenario.critic_lb_parameter=1.0E-1 \
+scenario.critic_regularization_param=30000 \
+scenario.critic_learning_norm_threshold=1 \
scenario.critic_td_n=2 \
scenario.critic_batch_size=32 \
+scenario.critic_model.add_random_init_noise=True 
# +scenario.critic_model.weight_max=500.0 \
# +scenario.is_mean_weighted=True \

# Working
# python run_stable.py \
# +seed=range\(10\) \
# scenario=calf \
# scenario.N_iterations=30 \
# system=3wrobot_kin \
# scenario.critic_model.quad_matrix_type=full \
# --experiment=calf_3wrobot_kin \
# +scenario.critic_safe_decay_param=1 \
# +scenario.critic_lb_parameter=1.0E-1 \
# +scenario.critic_regularization_param=30000 \
# +scenario.critic_learning_norm_threshold=1 \
# scenario.critic_td_n=2 \
# scenario.critic_batch_size=32 \
# +scenario.critic_model.add_random_init_noise=True 