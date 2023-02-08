"""
Python Programming (ACFI827-202223)
Assignment 1: Simulate Political Email Transactions in Blockchain
Created on Wed Nov 30 10:11:44 2022

"""

# =============================================================================
# Task A: Total number of emails and compare dictionary keys
# =============================================================================

# Modules below are imported to solve tasks in this assignment:
import math # To calculate formula in proof of work algorithm
import random # To randomly select 120 emails to solve Task C4
import datetime # To find current date and time
import sys # To exit from the code if an error occurs
import hashlib as _hashlib # To calculate hash value
import json as _json # To import json file data

# This code starts with Try and ends with Exceptions to raise and handle some errors may occur when users run this code. If no errors happen, codes will be executed successfully
try:
    # Firstly, import data to Python:
    jsonFilePath = '/Users/nguyenthidieulinh/Downloads/political-emails.json'  # This is where I save the file in my computer
    with open(jsonFilePath) as json_file: 
        json_data = _json.load(json_file) 
        
    # Data is imported successfully, below is solutions for each task
   
    """ 
    comments: Len function is used to find number of emails in dataset
    """
    Number_emails = len(json_data) # Emails are small objects in dataset, so number of emails is equal to the length of jsondata. Use function len to return the length of data
    print('Number of political emails in the dataset is ',Number_emails,' emails') # Print function to show the output

    """ 
    comments: For loop is written to compare keys of each email  
    """
    for i in range(len(json_data)):
    # Compare keys of each email to keys of first email, if at least one pair is not equal, exit code and show error message, if they are all equal, pass function and print result
        if json_data[0].keys() != json_data[i].keys(): 
            sys.exit('Keys of dictionary are not identical') 
        else: 
            pass 
    print ('Keys of dictionary are identical') # Print function to show the output

    """ 
    # Output:
        Number of political emails in the dataset is  406  emails
        Keys of dictionary are identical

    """

# =============================================================================
# Task B: Compare the hash value 
# =============================================================================
    """ 
    comments: Function hash_value is built to calculate hash value of an object
    """

    def hash_value(email_object):
        '''
        Function to encode string to a bytes object and hash to a value of 256 bits long
        Parameters: email object
        Returns: hash value of email object
        '''
        encoded_block = str(email_object).encode() # encode the string to a bytes object 
        hash_value = _hashlib.sha256(encoded_block).hexdigest() # SHA-256 is cryptographic hash function that outputs a value of 256 bits long
        return hash_value

    #Call function hash_value to compute hash value of 9th email and assign it to variable hashvalue1
    hashvalue1 = hash_value(json_data[8])
    # Re-compute hash value of 9th mail and assign it to variable hashvalue2
    hashvalue2 = hash_value(json_data[8])
    #Call function hash_value to compute hash value of 11th email and assign it to variable hashvalue3
    hashvalue3 = hash_value(json_data[10])

    # Write conditional statement to compare hashvalue1 and hashvalue2 and hashvalue1 and hashvalue3:
    if hashvalue1 == hashvalue2: 
        print('hashvalue1 and hashvalue2 are identical') #Print function to show the output
    else: 
        print('hashvalue1 and hashvalue2 are not identical') 
    if hashvalue1 == hashvalue3: 
        print('hashvalue1 and hashvalue3 are identical') #Print function to show the output
    else: 
        print('hashvalue1 and hashvalue3 are not identical') 

    """ 
    # Output:
        hashvalue1 and hashvalue2 are identical
        hashvalue1 and hashvalue3 are not identical

    """

# =============================================================================
# Task C1: Write Python function to create dictionary of a block 
# =============================================================================

# Task C1.1: Create a function to store block's information: 

    def create_block(index,time,data,proof,Hash):
        '''
        Function to create block to store information
        Parameters: informations of a block
        Returns: a dictionary datatype containing information of a block
        '''
        block = {'block_index': index,
                     'Transaction_time_stamp': time,
                     'transaction_data': data,
                     'proof_of_work': proof,
                     'previous_hash': Hash}
        return block
    
    print(help(create_block)) # Print information about function create_block

# Task C1.2: Write a function to store all blocks created

    def create_chain(block):
        '''
        Function to append new block to the blockchain
        Parameters: new block to add
        Returns: new chain that contains new block 
        '''
        chain=[] # Initialise an empty list
        chain.append(block) # when new block is created, add it to the chain 
        return chain # Return new chain 
    
    print(help(create_chain)) # Print information about function create_chain
    
    """ 
    # Output:
        Help on function create_block in module __main__:

        create_block(index, time, data, proof, Hash)
            Function to create block to store information
            Parameters: informations of a block
            Returns: a dictionary datatype containing information of a block

        None
        Help on function create_chain in module __main__:

        create_chain(block)
            Function to append new block to the blockchain
            Parameters: new block to add
            Returns: new chain that contains new block

        None

    """

# =============================================================================
# Task C2: Create a genesis block (first block in the chain) 
# =============================================================================
    """ 
    comments: Functions create_block() and  create_chain() in task C1 are called to create genesis block and blockchain
    """

    # Values of genesis block:
    # Block index = 1
    # Transaction time stamp => use function str(datetime.datetime.now() to display the current date and time
    # Transaction data = "This is the genesis block of email transactions."
    # Proof of work = 1
    # Hash of the previous block = "000" 
    # Create genesis block with above values by calling function create_block():

    genesis_block = create_block(1, str(datetime.datetime.now()),"This is the genesis block of email transactions.",1,'000')
    print(genesis_block) # Print function to show the output

    # Call function create_chain() to initialise the blockchain by adding a genesis block 
    Block_chain = create_chain(genesis_block)
    print(Block_chain) # Print function to show the output

    """ 
    # Output:
        {'block_index': 1, 'Transaction_time_stamp': '2022-12-07 10:24:41.740607', 'transaction_data': 'This is the genesis block of email transactions.', 'proof_of_work': 1, 'previous_hash': '000'}
        [{'block_index': 1, 'Transaction_time_stamp': '2022-12-07 10:24:41.740607', 'transaction_data': 'This is the genesis block of email transactions.', 'proof_of_work': 1, 'previous_hash': '000'}]
    """

# =============================================================================
# Task C3: Blockchain Mining - the process of adding transaction records to the blockchain 
# =============================================================================

    # To mine a new block, Proof of work has to be calculated correctly
    # Proof of work i calculated in two ways:
    # Way 1 (Task C3.1): proof_of_work is a random integer number between 2000 to 7000. Hence, proof_of_work = random.randint(2000,7001)
    # Way 2 (Task C3.2): Proof of work algorithm. In this assignment, proof of work algorithm will be used for mining a new block

     
    # Build function to calculate proof of work value according to algorithm
    def proof_of_work_algo(email_object, i):
        '''
        Function will run a loop to find the correct value of proof_of_work that matchs the rule required
        Parameters: email object that is accessing and the index position 
        Returns the correct value of proof_of_work
        '''
        previous_block = Block_chain[-1] # Because we are adding new block, previous block is the last block in the current blockchain, access it through negative indexing
        previous_proof = previous_block['proof_of_work'] # Get the previous_proof to calculate algorithm
       
        # Initialize a loop variable
        new_proof_of_work = 1
        check_proof = False
        
        # This loop is run until the correct value was found
        while check_proof is False:
            # Below is the algorithm for proof of work
            x = math.pow(new_proof_of_work, 3) + math.pow(previous_proof, 2) + i
            y = str(x) + email_object['datetime'] + ", " + email_object['email_id'] # y is string concatination of x and transaction data in block           
            z_hash_value = hash_value(y) # Call hash value function to calculate for hash of y
            
            # Rule of algorithm: if first three values of z_hash_value is equal to '000', the proof of work is correct
            if z_hash_value[:3] == '000':
                check_proof = True
            # If first three values is not '000', increase new_proof_of_work by one unit and continue searching
            else:           
                new_proof_of_work += 1
        return new_proof_of_work
    
    print(help(proof_of_work_algo)) # Print information about function proof_of_work_algo

    # Build function to mine new block
    def mine_block(email_object, previous_email_object, i):
        '''
        Function to create new block that contains transactional record data and add to the chain
        Parameters: email object that is accessing, the previous email, the index position of current email
        Returns blockchain which appends new block that has been just created
        '''
        block_index = len(Block_chain) + 1 # New block index is current number of blocks in blockchain plus 1
        transaction_time_stamp = str(datetime.datetime.now()) # use this function to display the current date and time
        transaction_data = email_object['datetime']+ ", " +email_object['email_id'] # Achieved by concatenating email sent date&time and email ID
        proof_of_work = proof_of_work_algo(email_object, i) # Call proof_of_work_algo function to calculate
        previous_hash = hash_value(previous_email_object) # Call hash_value function created in Task B to calculate hash of previous email
        
        # Call create_block function in Task C1.1 to create new block with above values
        new_block = create_block(block_index, transaction_time_stamp, transaction_data, proof_of_work, previous_hash)
        
        # Add new block to the Blockchain initialised in Task C2
        Block_chain.append(new_block)
        return Block_chain
    print(help(mine_block)) # Print information about function mine_block
    
    """ 
    # Output:
        Help on function proof_of_work_algo in module __main__:

        proof_of_work_algo(email_object, i)
            Function will run a loop to find the correct value of proof_of_work that matchs the rule required
            Parameters: email object that is accessing and the index position 
            Returns the correct value of proof_of_work

        None
        Help on function mine_block in module __main__:

        mine_block(email_object, previous_email_object, i)
            Function to create new block that contains transactional record data and add to the chain
            Parameters: email object that is accessing, the previous email, the index position of current email
            Returns blockchain which appends new block that has been just created

        None

    """

# =============================================================================
# Task C4: Simulate the storage of political email transaction in the blockchain 
# =============================================================================

    # Random function is used to randomly select 120 emails in json data to record in blockchain
    email_object = random.sample(json_data, 120)  

    # Create the main function to avoid duplicating blocks and printing many blockchains. Whenever run this code, this main function will be executed first and only print 1 blockchain
    if __name__ == '__main__':
        print('Start mining...')
        for i in range(len(email_object)):
            Block_chain = mine_block(email_object[i], email_object[i-1], i) # Call function mine_block() to create 120 new blocks and add them to chain
        print(Block_chain) # Print function to show the output

    """ 
    # Output:
    Start mining...
    [{'block_index': 1, 'Transaction_time_stamp': '2022-12-12 02:23:36.125637', 'transaction_data': 'This is the genesis block of email transactions.', 'proof_of_work': 1, 'previous_hash': '000'}, {'block_index': 2, 'Transaction_time_stamp': '2022-12-12 02:23:36.125988', 'transaction_data': '01/11/2018 09:45, 259', 'proof_of_work': 1969, 'previous_hash': 'c8ecc024383a2a58d0b5c553e876a8c1ac528614db052a274208ad5be0fb8a2d'}, {'block_index': 3, 'Transaction_time_stamp': '2022-12-12 02:23:36.130039', 'transaction_data': '13/09/2018 08:33, 41', 'proof_of_work': 1812, 'previous_hash': '6dd46afd4714326f75df895f88fdcc4c450f9709ddbf99893e6130a7006eb680'}, {'block_index': 4, 'Transaction_time_stamp': '2022-12-12 02:23:36.133642', 'transaction_data': '23/03/2018 10:06, 220', 'proof_of_work': 7, 'previous_hash': 'a49d9cbb23363621a13fd123210189c333907898d77bab87d2d9fc981539a3de'}, {'block_index': 5, 'Transaction_time_stamp': '2022-12-12 02:23:36.133676', 'transaction_data': '11/12/2017 06:54, 209', 'proof_of_work': 2092, 'previous_hash': '6a8258032b784c7f55edabcd402179564ad7e60fd3599a3466eddd6320d3b691'}, {'block_index': 6, 'Transaction_time_stamp': '2022-12-12 02:23:36.137591', 'transaction_data': '06/11/2018 14:00, 53', 'proof_of_work': 2498, 'previous_hash': '26def1dd8aa597f0df863b5d82dfb8172a9cc2b53af8e52ff73684a2dcc48955'}, {'block_index': 7, 'Transaction_time_stamp': '2022-12-12 02:23:36.142372', 'transaction_data': '03/08/2017 13:31, 394', 'proof_of_work': 5692, 'previous_hash': '9487a4038f26ed7fea5b8b5f29ccbdd9930fe4230dc6ac3a251e69b3839640c2'}, {'block_index': 8, 'Transaction_time_stamp': '2022-12-12 02:23:36.153021', 'transaction_data': '26/02/2018 18:32, 216', 'proof_of_work': 9529, 'previous_hash': 'd769e94d5178542758e72be423ca39b4bd5b494c7beec782c84126a140cfe89e'}, {'block_index': 9, 'Transaction_time_stamp': '2022-12-12 02:23:36.170228', 'transaction_data': '28/12/2017 12:37, 405', 'proof_of_work': 74, 'previous_hash': 'e5c9dae195a18a73b2b36a91d137e2dd702a8cbb280a4216f5f03312bfeee78f'}, {'block_index': 10, 'Transaction_time_stamp': '2022-12-12 02:23:36.170371', 'transaction_data': '18/06/2020 16:17, 353', 'proof_of_work': 2933, 'previous_hash': 'c28e0cb95b4e0f125052ec774d2287420bc6a4a25170d90fe598a79a2431f4b4'}, {'block_index': 11, 'Transaction_time_stamp': '2022-12-12 02:23:36.175638', 'transaction_data': '05/10/2019 04:13, 100', 'proof_of_work': 5554, 'previous_hash': 'bcc7a5a8d134e2d19597b0ee30e99a57221a096b458aeb7e37811b0059730ece'}, {'block_index': 12, 'Transaction_time_stamp': '2022-12-12 02:23:36.185618', 'transaction_data': '11/06/2020 12:18, 349', 'proof_of_work': 3609, 'previous_hash': '9929300fa01cbbc5c9143cf80b415f398b85957fe6ff949c87b6c24c7559fbee'}, {'block_index': 13, 'Transaction_time_stamp': '2022-12-12 02:23:36.192016', 'transaction_data': '15/10/2020 08:05, 384', 'proof_of_work': 13451, 'previous_hash': 'a3b1fba077922521cf92b9a5f176a4757af312283cf115823ca74201268059df'}, {'block_index': 14, 'Transaction_time_stamp': '2022-12-12 02:23:36.216132', 'transaction_data': '29/01/2019 12:31, 264', 'proof_of_work': 2819, 'previous_hash': '067d9bc2882b962c6453e3e0b907d563dc209ef2e445ca3de0aa40b097ad6aa1'}, {'block_index': 15, 'Transaction_time_stamp': '2022-12-12 02:23:36.221117', 'transaction_data': '10/07/2020 16:30, 356', 'proof_of_work': 1028, 'previous_hash': 'e8010a03503f5a4276c28e89d09ea204ccef7db192a211aa8bbbb661e96ae4c7'}, {'block_index': 16, 'Transaction_time_stamp': '2022-12-12 02:23:36.222922', 'transaction_data': '31/08/2019 13:15, 92', 'proof_of_work': 5048, 'previous_hash': '79cccbe6e942b21079a37c994515db4cf9a8b45322cacd7c157f92348f3cb483'}, {'block_index': 17, 'Transaction_time_stamp': '2022-12-12 02:23:36.231963', 'transaction_data': '14/04/2020 16:09, 148', 'proof_of_work': 2748, 'previous_hash': '3c3631fc6e06b534d51a49e6783bdf47b88ac2ab981ae9d6b0a02ef60ec59b6a'}, {'block_index': 18, 'Transaction_time_stamp': '2022-12-12 02:23:36.236844', 'transaction_data': '13/04/2018 08:07, 18', 'proof_of_work': 1371, 'previous_hash': '857bd140219f3ed7b808718fb695238ad1bc53cdd50fdedfc07ab1352271fa57'}, {'block_index': 19, 'Transaction_time_stamp': '2022-12-12 02:23:36.239319', 'transaction_data': '17/10/2017 05:20, 207', 'proof_of_work': 1330, 'previous_hash': '3cb842be08cffd5ed528597719136f409fdf5b1f07bbb1ebd37e013961d1656f'}, {'block_index': 20, 'Transaction_time_stamp': '2022-12-12 02:23:36.241677', 'transaction_data': '30/10/2018 08:09, 52', 'proof_of_work': 4287, 'previous_hash': '08abe35f2d4444e276339dbe7aa52a92602cad5d95a74104d418f394f1e5575f'}, {'block_index': 21, 'Transaction_time_stamp': '2022-12-12 02:23:36.249358', 'transaction_data': '06/04/2020 11:03, 333', 'proof_of_work': 13116, 'previous_hash': '77566e3a12713e02e2377949d58229f112da9df9b9a83ca83f42c6e312d7ef94'}, {'block_index': 22, 'Transaction_time_stamp': '2022-12-12 02:23:36.272994', 'transaction_data': '16/06/2020 14:51, 171', 'proof_of_work': 2863, 'previous_hash': '01bdfe053cbf7389a7e2eb4a4a201702a637f8d9721e5d35f18a7c1058aaba55'}, {'block_index': 23, 'Transaction_time_stamp': '2022-12-12 02:23:36.278024', 'transaction_data': '28/06/2018 09:00, 236', 'proof_of_work': 293, 'previous_hash': 'f8e33087c992b790c349ec3a6cd34b5f4b770849603d953bab145f86d5fc0580'}, {'block_index': 24, 'Transaction_time_stamp': '2022-12-12 02:23:36.278549', 'transaction_data': '15/01/2020 12:04, 321', 'proof_of_work': 7910, 'previous_hash': 'ed7fe80d325a8dc6fbdd5423c326eab45087252e1eae3fd54c32146b7f9276bf'}, {'block_index': 25, 'Transaction_time_stamp': '2022-12-12 02:23:36.293024', 'transaction_data': '11/02/2020 17:36, 132', 'proof_of_work': 4626, 'previous_hash': 'f7a9338985df052fb2d533600a39f0ec10ea42b48c1bdb7e5cec6c7289c533f6'}, {'block_index': 26, 'Transaction_time_stamp': '2022-12-12 02:23:36.301383', 'transaction_data': '28/04/2017 11:39, 79', 'proof_of_work': 2828, 'previous_hash': 'bc2e7bcbd8b330af3787a84368756cb52278772ea01a9b6386c93bbbb56d945f'}, {'block_index': 27, 'Transaction_time_stamp': '2022-12-12 02:23:36.306469', 'transaction_data': '18/09/2019 07:52, 291', 'proof_of_work': 14894, 'previous_hash': 'e6d4bb4e62470c0a25724d6f82c68a4dbea6de7b1571b8070fdab9fcbc4d41b0'}, {'block_index': 28, 'Transaction_time_stamp': '2022-12-12 02:23:36.334229', 'transaction_data': '20/09/2018 17:12, 250', 'proof_of_work': 6816, 'previous_hash': '50c69f3a00ade0f2b2c378d06d3bfefcdc1b3ef73e541e444d736fd41a584f9f'}, {'block_index': 29, 'Transaction_time_stamp': '2022-12-12 02:23:36.346523', 'transaction_data': '21/08/2020 09:14, 368', 'proof_of_work': 3603, 'previous_hash': '1e25a132bb9cedc4d33a29f42d65425c775e4311036bcd8ede140b7730c0bdde'}, {'block_index': 30, 'Transaction_time_stamp': '2022-12-12 02:23:36.352955', 'transaction_data': '04/06/2020 12:52, 167', 'proof_of_work': 8348, 'previous_hash': 'a0155a6076560261afa6d563e2304dd445bcf67b2eeb43ee9e1e69aa0d3bbc06'}, {'block_index': 31, 'Transaction_time_stamp': '2022-12-12 02:23:36.367820', 'transaction_data': '07/11/2019 07:10, 108', 'proof_of_work': 2811, 'previous_hash': '92f2728009ca07a4be9405f19b7f50edad5bd29cd18eee1c503a12824bcb104c'}, {'block_index': 32, 'Transaction_time_stamp': '2022-12-12 02:23:36.372841', 'transaction_data': '25/03/2020 12:55, 142', 'proof_of_work': 237, 'previous_hash': '0612719148eab7f10c091cd8c3c30e358120be105759cae147ba3db4564e6e1b'}, {'block_index': 33, 'Transaction_time_stamp': '2022-12-12 02:23:36.373313', 'transaction_data': '23/02/2018 08:06, 215', 'proof_of_work': 10822, 'previous_hash': '02fedaa2edb97d2d4563eeefe6d6e41a5b95fb6c3ca2d11587ca1086ea2562ce'}, {'block_index': 34, 'Transaction_time_stamp': '2022-12-12 02:23:36.392604', 'transaction_data': '15/05/2019 14:29, 61', 'proof_of_work': 2375, 'previous_hash': '73cbe9736f410bef30a9ee0e33668c9bd889e6a70766415c2f3873e46268c899'}, {'block_index': 35, 'Transaction_time_stamp': '2022-12-12 02:23:36.396795', 'transaction_data': '25/12/2019 11:20, 317', 'proof_of_work': 5931, 'previous_hash': '7458a190abac2585a30f095d8770e61be992de7ce97811f0bff4a4cfa7736780'}, {'block_index': 36, 'Transaction_time_stamp': '2022-12-12 02:23:36.407393', 'transaction_data': '30/03/2020 14:17, 331', 'proof_of_work': 6512, 'previous_hash': 'baf5c22610eaa7ffcca54279fe77f0e6b49fda213da30d066d80e94acb5b7b75'}, {'block_index': 37, 'Transaction_time_stamp': '2022-12-12 02:23:36.418932', 'transaction_data': '30/04/2020 13:09, 158', 'proof_of_work': 1081, 'previous_hash': '91fab124942ca3bbd02bd5d633fc08fcd5d8a7f9110dc49e238ab0325ec3971e'}, {'block_index': 38, 'Transaction_time_stamp': '2022-12-12 02:23:36.420840', 'transaction_data': '21/11/2017 05:03, 401', 'proof_of_work': 94, 'previous_hash': '778a93688d5b34bdb2b86a1c7a0010a3fa839304ac9d127e708b241b72c986a4'}, {'block_index': 39, 'Transaction_time_stamp': '2022-12-12 02:23:36.421010', 'transaction_data': '13/07/2020 07:28, 182', 'proof_of_work': 1208, 'previous_hash': 'faedbc1cba8054a06dc107570c35eecf2a5f35016563bf17f1d6dc120cfc5a85'}, {'block_index': 40, 'Transaction_time_stamp': '2022-12-12 02:23:36.423120', 'transaction_data': '17/09/2019 16:57, 96', 'proof_of_work': 1072, 'previous_hash': '904eb0dede37764e5061b7853d7e35066150baab405f682b4cbed24d34388aa7'}, {'block_index': 41, 'Transaction_time_stamp': '2022-12-12 02:23:36.425007', 'transaction_data': '07/01/2019 06:56, 57', 'proof_of_work': 11304, 'previous_hash': 'aff17b9dbfcda9d4cefa6b6756528d258dcbeeb7c29d3558d28647d2f604ceeb'}, {'block_index': 42, 'Transaction_time_stamp': '2022-12-12 02:23:36.445217', 'transaction_data': '25/12/2018 08:30, 262', 'proof_of_work': 8878, 'previous_hash': 'd880fcf0183bcff7bff6595eb608e3b30d58b0f2f8acba2323412b22b0a85f55'}, {'block_index': 43, 'Transaction_time_stamp': '2022-12-12 02:23:36.461058', 'transaction_data': '23/08/2020 12:24, 369', 'proof_of_work': 680, 'previous_hash': 'c1776dd50934b52ec7e58a0a9cbd9663efc5e24730f98846d5a18f71c4484ed8'}, {'block_index': 44, 'Transaction_time_stamp': '2022-12-12 02:23:36.462279', 'transaction_data': '17/06/2019 07:52, 273', 'proof_of_work': 1123, 'previous_hash': '53b2ea680be2170e51b33589590ef76cae297b819707d4ea0814a46f295ba5cc'}, {'block_index': 45, 'Transaction_time_stamp': '2022-12-12 02:23:36.464277', 'transaction_data': '27/10/2019 14:32, 299', 'proof_of_work': 6255, 'previous_hash': 'ebdf5bd9dcd1c5f6617f629edd0d18cc319efd512b0df92477d4e9cb7d0f919d'}, {'block_index': 46, 'Transaction_time_stamp': '2022-12-12 02:23:36.475344', 'transaction_data': '13/07/2018 08:38, 238', 'proof_of_work': 7203, 'previous_hash': '4d4a0ccab21a37105e39e11d8c2c86ff59a69855d4ff3ed940e9abe7c1529a88'}, {'block_index': 47, 'Transaction_time_stamp': '2022-12-12 02:23:36.488301', 'transaction_data': '07/10/2018 08:30, 44', 'proof_of_work': 1503, 'previous_hash': '2b211898954e83b7d9afc2a8ab116b01c7c6ef69018c89fc2bda14215c1d14df'}, {'block_index': 48, 'Transaction_time_stamp': '2022-12-12 02:23:36.490921', 'transaction_data': '17/04/2020 11:45, 334', 'proof_of_work': 2322, 'previous_hash': 'd540ff92a91d50304f7e1414aae1a0812e64cd2b75ef7c99015502ec93f0c7b4'}, {'block_index': 49, 'Transaction_time_stamp': '2022-12-12 02:23:36.495118', 'transaction_data': '03/12/2019 09:03, 313', 'proof_of_work': 3113, 'previous_hash': 'd6b082f7526af0905b34f0e3d1d673fc0f271ce2f3a501c4a4e01c041c150f0e'}, {'block_index': 50, 'Transaction_time_stamp': '2022-12-12 02:23:36.500760', 'transaction_data': '14/07/2020 16:00, 357', 'proof_of_work': 7544, 'previous_hash': '7aaa4909c8b845df17583a5cd3970bf158331e7eaf4a642781fe0778c560a4e3'}, {'block_index': 51, 'Transaction_time_stamp': '2022-12-12 02:23:36.514423', 'transaction_data': '06/11/2018 07:51, 260', 'proof_of_work': 1509, 'previous_hash': '705777a7de57be498a5f743443fd8362a51a251249345da41ee0dd839fbe3097'}, {'block_index': 52, 'Transaction_time_stamp': '2022-12-12 02:23:36.517106', 'transaction_data': '19/10/2019 10:56, 297', 'proof_of_work': 203, 'previous_hash': 'c50f8cd4c40ccfdb222810306ee2f5c5ea080de6776b75f2ba7c71bc763b6eab'}, {'block_index': 53, 'Transaction_time_stamp': '2022-12-12 02:23:36.517472', 'transaction_data': '02/08/2018 13:21, 33', 'proof_of_work': 1254, 'previous_hash': 'c431bc3f4e2f7dbeb80d91d21086379aa5e9901c3ef8630b366c18a600acb67c'}, {'block_index': 54, 'Transaction_time_stamp': '2022-12-12 02:23:36.519678', 'transaction_data': '07/12/2016 07:18, 306', 'proof_of_work': 232, 'previous_hash': '493a7b5af5693c2eb19f007f3cbfdf0e4b56189ab48a1c4c24f7c78f43a30a23'}, {'block_index': 55, 'Transaction_time_stamp': '2022-12-12 02:23:36.520097', 'transaction_data': '19/05/2018 07:29, 21', 'proof_of_work': 3913, 'previous_hash': 'f48a77fb8a999126bb84054a70f2fdb9bfaa474ce1fd5267fab74dbed22c643c'}, {'block_index': 56, 'Transaction_time_stamp': '2022-12-12 02:23:36.527021', 'transaction_data': '06/05/2020 08:08, 159', 'proof_of_work': 2731, 'previous_hash': 'f5c089547bbfefe9b6536e1b472f25cae8b22c7da19ae8536c3a12037bb64bcf'}, {'block_index': 57, 'Transaction_time_stamp': '2022-12-12 02:23:36.531872', 'transaction_data': '31/12/2017 13:57, 212', 'proof_of_work': 227, 'previous_hash': '53efa1e2805a450a482bd74834b379e55bc2b8a164f46202b15a7f6ad7160c3b'}, {'block_index': 58, 'Transaction_time_stamp': '2022-12-12 02:23:36.532287', 'transaction_data': '05/07/2020 16:35, 354', 'proof_of_work': 12232, 'previous_hash': 'c9056e06d91f3d021c572eec2f151d954c7b6dc45d152e980454266bdc3c4c75'}, {'block_index': 59, 'Transaction_time_stamp': '2022-12-12 02:23:36.554047', 'transaction_data': '13/09/2017 15:16, 206', 'proof_of_work': 13280, 'previous_hash': 'cd383a45b4ae569585e3f23f80d73eab19ed90cc2821b8d3d6036d7586de54d6'}, {'block_index': 60, 'Transaction_time_stamp': '2022-12-12 02:23:36.577748', 'transaction_data': '29/04/2019 13:42, 60', 'proof_of_work': 1294, 'previous_hash': '35a68947fdfbc0afd1a7188f910170ea83146e75f982ac95db8db9d487a47919'}, {'block_index': 61, 'Transaction_time_stamp': '2022-12-12 02:23:36.580028', 'transaction_data': '13/06/2018 12:01, 23', 'proof_of_work': 2257, 'previous_hash': 'd8812214d2edd722a54f70b84b15adafd6dc7c5a7fa83171160c2641c76dcd67'}, {'block_index': 62, 'Transaction_time_stamp': '2022-12-12 02:23:36.583987', 'transaction_data': '27/10/2019 13:11, 104', 'proof_of_work': 12046, 'previous_hash': 'c6aff78903f95de085369626aa6f3179978920aaad83b42adf93a96ad4c1bb8b'}, {'block_index': 63, 'Transaction_time_stamp': '2022-12-12 02:23:36.605405', 'transaction_data': '30/06/2019 16:37, 280', 'proof_of_work': 11263, 'previous_hash': 'd1c5d7c1261699ec3534c39ac8eaccffc74e3b7d8eb4f90d5c6d6acfa80d6c42'}, {'block_index': 64, 'Transaction_time_stamp': '2022-12-12 02:23:36.639233', 'transaction_data': '30/07/2019 17:19, 284', 'proof_of_work': 3472, 'previous_hash': 'd5fca14ed7eafb99349e224edc28424b496ec98e3cb0ee1c01e8351cad405640'}, {'block_index': 65, 'Transaction_time_stamp': '2022-12-12 02:23:36.646258', 'transaction_data': '20/05/2020 12:12, 164', 'proof_of_work': 417, 'previous_hash': 'b09d4a86050fad4c44dafe462316f7e77868d89a2fc255b1c2f90679fd20a812'}, {'block_index': 66, 'Transaction_time_stamp': '2022-12-12 02:23:36.647052', 'transaction_data': '20/06/2019 15:15, 276', 'proof_of_work': 6818, 'previous_hash': '687bdc5087f4ca63b32ba980a08310b219d0f47e4759e13c5a3da2aaaad4fafd'}, {'block_index': 67, 'Transaction_time_stamp': '2022-12-12 02:23:36.659943', 'transaction_data': '18/03/2020 07:16, 141', 'proof_of_work': 126, 'previous_hash': 'b975ba726c95116a2c221583a739b1ee96c3e39f8a343921c9643e0590c4a2f8'}, {'block_index': 68, 'Transaction_time_stamp': '2022-12-12 02:23:36.660208', 'transaction_data': '27/12/2017 12:31, 9', 'proof_of_work': 12411, 'previous_hash': 'ded1f3cd2aa333552a7844cbc904c6759bd2663440f8752d57f7dd6548462614'}, {'block_index': 69, 'Transaction_time_stamp': '2022-12-12 02:23:36.683044', 'transaction_data': '05/06/2020 15:02, 168', 'proof_of_work': 16172, 'previous_hash': '80979c74fa3e580839a45cbd43aa89151e877d4d9f25f3e2ff6772b4ccf83f3d'}, {'block_index': 70, 'Transaction_time_stamp': '2022-12-12 02:23:36.712448', 'transaction_data': '24/08/2020 14:00, 373', 'proof_of_work': 4003, 'previous_hash': '0f7d393f065d3bbbf4c1c943139b1c5b639e9af6acd1d7cd4dec280a4a2197f2'}, {'block_index': 71, 'Transaction_time_stamp': '2022-12-12 02:23:36.719588', 'transaction_data': '27/12/2019 14:04, 122', 'proof_of_work': 3223, 'previous_hash': 'cd0af87aca82c8c8a5afa2096dfe3095457e8c5df7283dbf51d3e072f8d5e492'}, {'block_index': 72, 'Transaction_time_stamp': '2022-12-12 02:23:36.725289', 'transaction_data': '02/10/2019 10:18, 294', 'proof_of_work': 3092, 'previous_hash': '5d9c0b4ffa970f3a107a1fbe02834eaf045a56e539a75336210f27673a8b1433'}, {'block_index': 73, 'Transaction_time_stamp': '2022-12-12 02:23:36.730759', 'transaction_data': '17/12/2020 08:56, 252', 'proof_of_work': 3177, 'previous_hash': '12acdab6d20dafe72ecab6b5c28dbc26010b0ff2a0bf6c924ecbc9b73f708eb2'}, {'block_index': 74, 'Transaction_time_stamp': '2022-12-12 02:23:36.736343', 'transaction_data': '13/06/2018 07:01, 227', 'proof_of_work': 1194, 'previous_hash': '3e705748cd98df10974076b73ef547ce742b0a058a839e9e7be780f1113f28fe'}, {'block_index': 75, 'Transaction_time_stamp': '2022-12-12 02:23:36.738488', 'transaction_data': '31/10/2018 09:30, 258', 'proof_of_work': 2311, 'previous_hash': '464c918d3a7c4cdb3905efd86b377e1d9e34340f0a9f3b20191906b54c4aca63'}, {'block_index': 76, 'Transaction_time_stamp': '2022-12-12 02:23:36.742560', 'transaction_data': '12/07/2018 16:09, 30', 'proof_of_work': 1656, 'previous_hash': 'd7ec96f88eb3b8cecc2fe287ab982ede9234f50fd851b98c106495742c72f588'}, {'block_index': 77, 'Transaction_time_stamp': '2022-12-12 02:23:36.745476', 'transaction_data': '13/07/2020 09:50, 181', 'proof_of_work': 4176, 'previous_hash': '388cb053448974c45d330fdf5307a15597e8a74c5430ebab5f4e02be0faec219'}, {'block_index': 78, 'Transaction_time_stamp': '2022-12-12 02:23:36.752889', 'transaction_data': '12/07/2020 17:31, 183', 'proof_of_work': 10433, 'previous_hash': '51d98ef213c3972e7365b3464fd05cafc3e4a7cf8206d37655f34b0cb9b40937'}, {'block_index': 79, 'Transaction_time_stamp': '2022-12-12 02:23:36.771409', 'transaction_data': '23/10/2017 12:22, 397', 'proof_of_work': 7133, 'previous_hash': 'd7901c5252dd8a265d2ff21414f716d049fae9595ccca0ce6836962678ee579d'}, {'block_index': 80, 'Transaction_time_stamp': '2022-12-12 02:23:36.784123', 'transaction_data': '26/06/2018 08:23, 232', 'proof_of_work': 4336, 'previous_hash': 'b19f6a813e3dd6e10bf783f5b1863a523ffd429e1a2affc96aa275ba684da8cb'}, {'block_index': 81, 'Transaction_time_stamp': '2022-12-12 02:23:36.791819', 'transaction_data': '29/09/2019 08:12, 98', 'proof_of_work': 5440, 'previous_hash': 'e232491bc1a69183021bae9436ceac0e44e1431c4687988e57bbc2c89fd15ae5'}, {'block_index': 82, 'Transaction_time_stamp': '2022-12-12 02:23:36.801638', 'transaction_data': '25/11/2019 10:46, 310', 'proof_of_work': 9317, 'previous_hash': 'fc1fbf4101663566fa579a1e0edc5d35d488346f0c07f465f8230cc2a3ff934f'}, {'block_index': 83, 'Transaction_time_stamp': '2022-12-12 02:23:36.818929', 'transaction_data': '19/04/2020 14:11, 149', 'proof_of_work': 4867, 'previous_hash': 'c80a18f6522f6d4f0c8d7941ec0edd24e17630e218075a04b40246b50f5cc4d5'}, {'block_index': 84, 'Transaction_time_stamp': '2022-12-12 02:23:36.827932', 'transaction_data': '26/06/2018 06:25, 233', 'proof_of_work': 963, 'previous_hash': 'b5a475f57d835611022d5c26170aec1dc6e64ee5dafe7d0bbd8a030c87db289a'}, {'block_index': 85, 'Transaction_time_stamp': '2022-12-12 02:23:36.829700', 'transaction_data': '14/02/2020 13:00, 134', 'proof_of_work': 14808, 'previous_hash': 'c908a0f4bd061ee05ae9fac558388e83f74c27ab435f3c6995b2bbc4810e672d'}, {'block_index': 86, 'Transaction_time_stamp': '2022-12-12 02:23:36.856333', 'transaction_data': '08/06/2017 16:01, 388', 'proof_of_work': 1297, 'previous_hash': 'f75d2aa88975918bfed6370b2e03f430870b916cb506c2213a298f4b4067d6f8'}, {'block_index': 87, 'Transaction_time_stamp': '2022-12-12 02:23:36.858699', 'transaction_data': '24/08/2019 11:31, 288', 'proof_of_work': 921, 'previous_hash': '24589bd810e9902ef531c89791c757e2a136601b66cf1e2070f86095e84c5b81'}, {'block_index': 88, 'Transaction_time_stamp': '2022-12-12 02:23:36.860383', 'transaction_data': '30/08/2018 11:11, 247', 'proof_of_work': 1987, 'previous_hash': '298a021c870537a6b2682bc44f3a897c95b502be6e5d6123dff248925cc2eaae'}, {'block_index': 89, 'Transaction_time_stamp': '2022-12-12 02:23:36.863889', 'transaction_data': '18/07/2017 14:14, 202', 'proof_of_work': 15233, 'previous_hash': '4e1675853c642948854df0409255d1c8a7c2a9ffaafcc487ef4c15df7e466cf8'}, {'block_index': 90, 'Transaction_time_stamp': '2022-12-12 02:23:36.891081', 'transaction_data': '28/05/2020 06:05, 165', 'proof_of_work': 2979, 'previous_hash': '944e850603787e31414ed999c33f05d6638ded349ca8232eb7326707a5c3fbc7'}, {'block_index': 91, 'Transaction_time_stamp': '2022-12-12 02:23:36.896487', 'transaction_data': '14/07/2017 13:17, 1', 'proof_of_work': 5324, 'previous_hash': '7780da2d38d428a37916c94204fcde2dee41ac711aa84768089f1f8ece4640ac'}, {'block_index': 92, 'Transaction_time_stamp': '2022-12-12 02:23:36.905985', 'transaction_data': '27/11/2019 18:29, 311', 'proof_of_work': 51, 'previous_hash': 'e9142ebc923404b2cd92d40e2995b40d03ff9aad10b1a47b920153ade007cf50'}, {'block_index': 93, 'Transaction_time_stamp': '2022-12-12 02:23:36.906132', 'transaction_data': '19/04/2019 19:15, 266', 'proof_of_work': 2566, 'previous_hash': '4bbb48c51b40873795f4282ce46b0cb8d3c6798a68701fcac282bbf94aed7aa2'}, {'block_index': 94, 'Transaction_time_stamp': '2022-12-12 02:23:36.910845', 'transaction_data': '23/06/2020 10:34, 173', 'proof_of_work': 8643, 'previous_hash': '4c76f880a5b53eca48c3fce25dc1287e4ae79974d85eeba68c29c7d8c6e170c6'}, {'block_index': 95, 'Transaction_time_stamp': '2022-12-12 02:23:36.926404', 'transaction_data': '02/11/2017 15:48, 7', 'proof_of_work': 15292, 'previous_hash': 'c5bffeae7136ce581fd33a1399db12a056582bbfa481cc2c826421571fa1cdbe'}, {'block_index': 96, 'Transaction_time_stamp': '2022-12-12 02:23:36.953645', 'transaction_data': '18/07/2020 12:46, 360', 'proof_of_work': 4820, 'previous_hash': '5eb432a3080cab61b8cb64b263dce8c367d0a0ccfec466e35463614ff570c4c1'}, {'block_index': 97, 'Transaction_time_stamp': '2022-12-12 02:23:36.962177', 'transaction_data': '04/10/2020 11:53, 381', 'proof_of_work': 6367, 'previous_hash': 'e55cd7a28c3bfcffb5693eb914618961cc2c9a1c8c4e8525df98b343371fb53d'}, {'block_index': 98, 'Transaction_time_stamp': '2022-12-12 02:23:36.973470', 'transaction_data': '05/09/2020 07:45, 200', 'proof_of_work': 14093, 'previous_hash': '6d3c2fac1af834fca6b740bcb3c33aa41f83666ea3a9abc114270cbe315a012b'}, {'block_index': 99, 'Transaction_time_stamp': '2022-12-12 02:23:36.998647', 'transaction_data': '23/05/2019 06:30, 62', 'proof_of_work': 3069, 'previous_hash': '32c40aebe057d2e6d4ee86d3c933b6149c78336f33ea45133a897ca4e5dd36d8'}, {'block_index': 100, 'Transaction_time_stamp': '2022-12-12 02:23:37.004059', 'transaction_data': '31/12/2019 18:52, 123', 'proof_of_work': 2812, 'previous_hash': 'aeacb7fe6d4e6acc398853a57b2d961f3b239b8c67515edd82b4f6fe16a52163'}, {'block_index': 101, 'Transaction_time_stamp': '2022-12-12 02:23:37.009041', 'transaction_data': '22/06/2018 14:02, 231', 'proof_of_work': 7388, 'previous_hash': 'bf946954fd5660e11ca6dadac901b313ea074351c4f403625a653d46b620aa58'}, {'block_index': 102, 'Transaction_time_stamp': '2022-12-12 02:23:37.022183', 'transaction_data': '04/07/2020 06:46, 180', 'proof_of_work': 4570, 'previous_hash': 'ba00c9b4c2dfbe2da162b83262f689c290e8db993896cb1ba6b543a63af1d593'}, {'block_index': 103, 'Transaction_time_stamp': '2022-12-12 02:23:37.030271', 'transaction_data': '02/09/2020 07:04, 196', 'proof_of_work': 971, 'previous_hash': '73019a6ed3f5213b445051bf673fa23a399c9e023066be0ff94fa48fe84bfb10'}, {'block_index': 104, 'Transaction_time_stamp': '2022-12-12 02:23:37.032030', 'transaction_data': '27/07/2020 10:24, 190', 'proof_of_work': 345, 'previous_hash': 'd33552db45aa437d19f971e38612ffeb6a5be4ae4e628d5c1f4edf186c572290'}, {'block_index': 105, 'Transaction_time_stamp': '2022-12-12 02:23:37.032662', 'transaction_data': '18/01/2018 12:36, 11', 'proof_of_work': 7625, 'previous_hash': '46ad46a0b0b933c126ac5373c3239c62b9be15e3069027ee81b37584406eeec8'}, {'block_index': 106, 'Transaction_time_stamp': '2022-12-12 02:23:37.046235', 'transaction_data': '03/12/2018 16:12, 55', 'proof_of_work': 13788, 'previous_hash': '7e6af3b3e8582202fe62c833f50a97c7d068641224264e6bd8f8202b39ee9d68'}, {'block_index': 107, 'Transaction_time_stamp': '2022-12-12 02:23:37.071031', 'transaction_data': '28/08/2019 16:26, 89', 'proof_of_work': 13623, 'previous_hash': 'bf77ff7a2a9f1f54cd2275a3e4db5ed0b42e34017ecdab1f26571419536bccf9'}, {'block_index': 108, 'Transaction_time_stamp': '2022-12-12 02:23:37.095408', 'transaction_data': '19/07/2018 06:13, 31', 'proof_of_work': 7337, 'previous_hash': 'fb3522d9c1a5b4ff2fc22c13d15e66b40e90626a2f1460cc9fd09f91b36a98ac'}, {'block_index': 109, 'Transaction_time_stamp': '2022-12-12 02:23:37.108547', 'transaction_data': '01/07/2018 16:58, 237', 'proof_of_work': 2105, 'previous_hash': '886d9fd517f6539094c84a2b74079a980f78247358d9efd0ce071ec9ac878c54'}, {'block_index': 110, 'Transaction_time_stamp': '2022-12-12 02:23:37.112242', 'transaction_data': '11/08/2019 10:12, 285', 'proof_of_work': 13194, 'previous_hash': '5563ba77daf81d78391a6d789a2d426820ed85df6ecbe70fb11d51d4295e00f3'}, {'block_index': 111, 'Transaction_time_stamp': '2022-12-12 02:23:37.136150', 'transaction_data': '11/06/2019 10:19, 72', 'proof_of_work': 8978, 'previous_hash': '9aac87653e0df67a41de6dd93ba6b089c1b589e41d07361f1a9b7c2089f900d6'}, {'block_index': 112, 'Transaction_time_stamp': '2022-12-12 02:23:37.152242', 'transaction_data': '15/06/2020 13:04, 170', 'proof_of_work': 1588, 'previous_hash': '895bd93fa4d672749fa9662d068f40285f581210b4f89734d261c0dd4e1796c8'}, {'block_index': 113, 'Transaction_time_stamp': '2022-12-12 02:23:37.155064', 'transaction_data': '19/11/2019 09:50, 113', 'proof_of_work': 5966, 'previous_hash': 'b336256303f68e6556ace50de1973eaee29cc19811b00123086d6656d05ee5d9'}, {'block_index': 114, 'Transaction_time_stamp': '2022-12-12 02:23:37.165881', 'transaction_data': '28/09/2018 17:08, 43', 'proof_of_work': 5528, 'previous_hash': 'b03373326794979e48c6ab180e622988e383a382dcdc7f8ce5bbe55a2dfe0b46'}, {'block_index': 115, 'Transaction_time_stamp': '2022-12-12 02:23:37.175844', 'transaction_data': '21/03/2018 14:01, 17', 'proof_of_work': 4898, 'previous_hash': '3e396441a39ff177dd98cab67b1d9e6ac113d1b02558b49aa141dd2805b1547f'}, {'block_index': 116, 'Transaction_time_stamp': '2022-12-12 02:23:37.184621', 'transaction_data': '26/07/2018 13:38, 32', 'proof_of_work': 1339, 'previous_hash': '4272c821a717e1c31523a01898e715e574a15ccfb43f8aaf2ae6e63d4e792cf4'}, {'block_index': 117, 'Transaction_time_stamp': '2022-12-12 02:23:37.187009', 'transaction_data': '24/05/2020 10:40, 346', 'proof_of_work': 5391, 'previous_hash': '93fd0a1c5b3442b9f7dd4c1a7fa7db94d31d886eca73172593d3d84310964ef6'}, {'block_index': 118, 'Transaction_time_stamp': '2022-12-12 02:23:37.196687', 'transaction_data': '25/08/2020 09:10, 194', 'proof_of_work': 8071, 'previous_hash': 'd5a01ec6c0ff0a0918746a68a7a2017879f7f5ad615c9d4ba15e0e274331a65f'}, {'block_index': 119, 'Transaction_time_stamp': '2022-12-12 02:23:37.211347', 'transaction_data': '27/04/2020 18:10, 153', 'proof_of_work': 75, 'previous_hash': '1056d6583794d88281880a104b669986d7b15cdeb7c3123e3bc850530ef87d0b'}, {'block_index': 120, 'Transaction_time_stamp': '2022-12-12 02:23:37.211549', 'transaction_data': '26/09/2019 10:04, 97', 'proof_of_work': 1321, 'previous_hash': 'e52f9f5b204568248d7c8ff3c9ff5be9200a2b2b9d1546b129324c3847b0333e'}, {'block_index': 121, 'Transaction_time_stamp': '2022-12-12 02:23:37.213928', 'transaction_data': '07/05/2020 06:39, 161', 'proof_of_work': 23958, 'previous_hash': 'd773bbd3a84d71f2b34c144f0aff41df0791b35befff88f5518459bdec68f26e'}]
    """ 
# Raise some errors may occur when users run this code
except FileNotFoundError: # When users do not have data in their computers or insert wrong data file path
    print('No data file found. Please check!')
except SystemExit: # When users input data which have different keys, which makes blockchain can not be build
    print('Cannot build blockchain because the keys of objects in data file are not identical')
except IndexError: # When users input wrong index while trying to access a block in chain
    print('Cannot access to block requested. Please check index of block in blockchain')
except ValueError: # When user input numbers of blocks to record exceed numbers of objects in data file or input a negative number
    print('Number of blocks requested to record are larger than data file or is a negative number')
except KeyError: # When users input data which lacks necessary information to calculate keys of a block
    print ('Lack necessary data to calculate keys for new block. Please input more data!')
else:
    print('Blocks are mined successfully')