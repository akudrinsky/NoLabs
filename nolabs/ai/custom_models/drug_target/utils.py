import os
import tarfile
import urllib.request
import rdkit.Chem as Chem
from rdkit.Chem import SDMolSupplier

dirname = os.path.dirname

import ssl

# Create an unverified SSL context
ssl._create_default_https_context = ssl._create_unverified_context


def install_p2rank():
    # URL of the p2rank tar.gz file
    p2rank_url = "https://github.com/rdk/p2rank/releases/download/2.4.1/p2rank_2.4.1.tar.gz"

    # P2Rank folder
    p2rank_folder = dirname(os.path.abspath(__file__)) + "/p2rank_2.4.1/"

    # Check if the destination folder already exists
    if os.path.exists(p2rank_folder):
        return

    destination_folder = dirname(os.path.abspath(__file__)) + "/"        

    # Create the destination folder
    os.makedirs(destination_folder, exist_ok=True)

    # Download the p2rank tar.gz file
    p2rank_tar_path = os.path.join(destination_folder, "p2rank.tar.gz")
    urllib.request.urlretrieve(p2rank_url, p2rank_tar_path)

    # Extract the contents of the tar.gz file
    with tarfile.open(p2rank_tar_path, "r:gz") as tar:
        tar.extractall(destination_folder)

    # Remove the downloaded tar.gz file
    os.remove(p2rank_tar_path)

    print("p2rank successfully installed and extracted to:", destination_folder)


def read_sdf_files(ligand_files_paths):
    # Initialize lists to store file names and SMILES strings
    file_names = []
    smiles_list = []

    # Iterate through files in the 'temp/' folder
    for file_path in ligand_files_paths:

        # Extract file name without the '.sdf' extension
        file_name_without_extension = os.path.splitext(os.path.basename(file_path))[0]

        # Initialize an SDMolSupplier to read the SDF file
        sdf_supplier = SDMolSupplier(file_path)

        # Iterate through molecules in the SDF file and convert to SMILES
        for mol in sdf_supplier:
            if mol is not None:
                # Convert the molecule to SMILES and append to the list
                smiles = Chem.MolToSmiles(mol)
                file_names.append(file_name_without_extension)
                smiles_list.append(smiles)

    return file_names, smiles_list

def get_sequence(file):
    sequence = ''
    with open(file, 'r') as file:
        for line in file:
            if line.startswith('>'):
                continue  # Skip the header line
            sequence += line.strip()  # Append the sequence removing any whitespace
    return sequence