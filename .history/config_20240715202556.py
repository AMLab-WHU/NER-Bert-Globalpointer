import time

common = {
    "exp_name": "split_20",
    "encoder": "BERT",
    "data_home": "./datasets",
    "bert_path": "./pretrained_models/",  
    "run_type": "train",  
    "f1_2_save": 0.5,  
    "logger": "default" 
}
wandb_config = {
    "run_name": time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()),
    "log_interval": 10
}
train_config = {
    "train_data": "train.json",
    "valid_data": "val.json",
    "test_data": "val.json",
    "ent2id": "ent2id.json",
    "path_to_save_model": "./outputs", 
    "hyper_parameters": {
        "lr": 2e-5,
        "batch_size": 110,
        "epochs": 50,
        "seed": 2333,
        "max_seq_len": 256,
        "scheduler": "None"  
    }
}
eval_config = {
    "model_state_dir": "./outputs/split_1/",  
    "run_id": "",
    "last_k_model": 1, 
    "predict_data": "test2.json",
    "ent2id": "ent2id.json",
    "save_res_dir": "./results",
    "hyper_parameters": {
        "batch_size": 32,
        "max_seq_len": 256,
    }

}
cawr_scheduler = {
    "T_mult": 1,
    "rewarm_epoch_num": 2,
}
step_scheduler = {
    "decay_rate": 0.999,
    "decay_steps": 200,
}
# ---------------------------------------------
train_config["hyper_parameters"].update(**cawr_scheduler, **step_scheduler)
train_config = {**train_config, **common, **wandb_config}
eval_config = {**eval_config, **common}
