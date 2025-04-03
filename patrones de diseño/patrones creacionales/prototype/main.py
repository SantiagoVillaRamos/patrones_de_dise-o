
from concrete_prototype import SystemConfigClone

def main():
    config = {
        "Os":"Linux",
        "Version":"Ubuntu 18.04"  
    }
    original_config = SystemConfigClone(config)
    cloned_config = original_config.clonar()
    print(f"\nOriginal config: {original_config.configuracion}")
    print(f"Configuracion clonada: {cloned_config.configuracion}")
    

if __name__=="__main__":
    main()