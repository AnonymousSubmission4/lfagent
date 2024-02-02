python run_stable.py \
+seed=0,1,2,3,4,5,6,7,8,9 \
scenario=calf \
system=inv_pendulum \
--experiment=calf_inv_pendulum \
--jobs=-1 \
scenario.critic_model.quad_matrix_type=symmetric \
+scenario.critic_safe_decay_param=0.1 \
+scenario.critic_lb_parameter=1.0E-3 \
+scenario.critic_regularization_param=200000 \
+scenario.critic_learning_norm_threshold=1. \
scenario.critic_td_n=1 \
scenario.critic_batch_size=30 \
+scenario.critic_learning_norm_threshold=2.0 \
scenario.N_iterations=6 \
+scenario.critic_model.add_random_init_noise=True \
+scenario.store_weights_thr=2.5

# python run_stable.py \
# +seed=range\(10,20\) \
# scenario=calf \
# system=inv_pendulum \
# --experiment=calf_inv_pendulum \
# --jobs=-1 \
# scenario.critic_model.quad_matrix_type=symmetric \
# +scenario.critic_safe_decay_param=0.1 \
# +scenario.critic_lb_parameter=1.0E-3 \
# +scenario.critic_regularization_param=80000 \
# +scenario.critic_learning_norm_threshold=1. \
# scenario.critic_td_n=2 \
# scenario.critic_batch_size=10 \
# +scenario.critic_learning_norm_threshold=0.5 \
# scenario.N_iterations=30 \
# +scenario.critic_model.add_random_init_noise=True \
# +scenario.store_weights_thr=2.5 