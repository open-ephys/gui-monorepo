import os
import argparse
import subprocess
import shutil
import sys

def clean_environment(build_directory):
    if(os.path.exists(build_directory)):
        print("[Conda Dependency Installer] Cleaning {}".format(build_directory), flush=True)
        shutil.rmtree(full_env_directory_path)

def create_environment(build_directory, config_file_path, prefix):
    command = 'conda env create --prefix={} --file={}'.format(build_directory, config_file_path)
    if prefix != None:
        command= '{} {}'.format(prefix, command)
    print("[Conda Dependency Installer] Running {}".format(command), flush=True)
    cp = subprocess.run(command, shell=True)
    return cp.returncode

if __name__ == "__main__":
    #Parse command line arguements
    parser = argparse.ArgumentParser(description='Installs dependency libraries to build output directory')
    parser.add_argument('-o', '--output-dir', help='Directory in which to place the locally installed conda environment', required=True)
    parser.add_argument('-e', '--env', help='Environment configuration to be installed', required=True)
    parser.add_argument('-c', '--clean', action='store_true', help="Clean dependency env before installing")
    parser.add_argument('-p', '--prefix', help='Prefix arguments to conda CMD')

    args = parser.parse_args()

    #Validate monorepo build directory exists
    build_directory = args.output_dir

    if(args.clean):
        clean_environment(build_directory)

    if os.path.exists(os.path.join(build_directory)):
        print("[Conda Dependency Installer] {} already exists; run with -c to clean or delete directory before build to re-install conda dependencies if desired".format(build_directory), flush=True)
        sys.exit(0)

    print("[Conda Dependency Installer] Setting build directory to {}".format(build_directory), flush=True)
    os.makedirs(build_directory, exist_ok=True)

    #Validate config env file exists
    current_path_name = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(current_path_name, args.env)
    print("[Conda Dependency Installer] Using env config file {}".format(config_file_path), flush=True)
    assert os.path.isfile(config_file_path), "Env config file does not exist"

    returncode = create_environment(build_directory, config_file_path, args.prefix)
    sys.exit(returncode)
