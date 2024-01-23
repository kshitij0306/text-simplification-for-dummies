from run_with_scheduler import *
def ssh_train(base_path="./", src_train="dataset/INT.txt", tgt_train="dataset/ELE.txt",
              src_valid="dataset/src_valid.txt", tgt_valid="dataset/tgt_valid.txt",
              ref_valid="dataset/ref_valid.pkl", checkpoint_path="cp_ele_int/model_ckpt.pt",
              best_model="cp_ele_int/model.pt", seed=540):
    train_kwargs = {
        "base_path": base_path,
        "src_train": src_train,
        "tgt_train": tgt_train,
        "src_valid": src_valid,
        "tgt_valid": tgt_valid,
        "ref_valid": ref_valid,
        "best_model": best_model,
        "checkpoint_path": checkpoint_path,
        "seed": seed
    }

    print(f"Starting training with following parameters: {train_kwargs}")
    logging.info(f"Starting training with following parameters: {train_kwargs}")

    # Call your train function with the kwargs
    train(**train_kwargs)

def ssh_train_with_scheduler(base_path="./", src_train="dataset/INT.txt", tgt_train="dataset/ELE.txt",
              src_valid="dataset/src_valid.txt", tgt_valid="dataset/tgt_valid.txt",
              ref_valid="dataset/ref_valid.pkl", checkpoint_path="cp_scheduler/model_ckpt.pt",
              best_model="cp_scheduler/model.pt", seed=540):

    train_kwargs = {
        "base_path": base_path,
        # "src_train": src_train,
        # "tgt_train": tgt_train,
        "src_valid": src_valid,
        "tgt_valid": tgt_valid,
        "ref_valid": ref_valid,
        "best_model": best_model,

        "src_train_level_1": "dataset/ELE_INT/ELE.txt",
        "tgt_train_level_1": "dataset/ELE_INT/INT.txt",

        "src_train_level_2": "dataset/ADV_INT/INT.txt",
        "tgt_train_level_2": "dataset/ADV_INT/ADV.txt",

        "src_train_level_3": "dataset/ADV_ELE/ELE.txt",
        "tgt_train_level_3": "dataset/ADV_ELE/ADV.txt",

        "checkpoint_path": checkpoint_path,
        "seed": seed
    }

    log_file_name = f"log_file_{datetime.now().strftime('%Y%m%d_%H%M%S')}_scheduler.log"
    logging.basicConfig(filename=log_file_name, level=logging.INFO,
                        format="%(asctime)s:%(levelname)s: %(message)s")
    print(f"Starting training with following parameters: {train_kwargs}")
    logging.info(f"Starting training with following parameters: {train_kwargs}")



    # Call your train function with the kwargs
    train(**train_kwargs)

if __name__  == "__main__":
    ssh_train_with_scheduler()