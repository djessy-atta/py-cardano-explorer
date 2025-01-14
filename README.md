# Python Cardano Explorer

Python wrapper for accessing and processing information stored on the Cardano blockchain using [Blockfrost API](https://blockfrost.io/).

<br />

**Table of contents**
- [Install](#Install)
- [Usage](#Usage)
- [Api Key](#Api-Key)
- [Using With Proxy](#Using-With-Proxy)
- [Network Info](#Network-Info)
  * [Network Informations](#Network-Informations)
- [Stake](#Stake)
  * [Stake Informations](#Stake-Informations)
  * [Stake Reward History](#Stake-Reward-History)
  * [Stake Rewards History Analysis](#Stake-Rewards-History-Analysis)
  * [Stake Amount History](#Stake-Amount-History)
  * [Stake Delegation History](#Stake-Delegation-History)
  * [Stake Registrations And Deregistrations History](#Stake-Registrations-And-Deregistrations-History)
  * [Stake Withdrawal History](#Stake-Withdrawal-History)
  * [Stake MIR History](#Stake-MIR-History)
  * [Stake Associated Addresses](#Stake-Associated-Addresses)
  * [Stake Assets Associated Addresses](#Stake-Assets-Associated-Addresses)
- [Address](#Address)
  * [Specific Address](#Specific-Address)
  * [Address Details](#Address-Details)
  * [Address UTXOs](#Address-UTXOs)
  * [Address Transactions](#Address-Transactions)
- [Epoch](#Epoch)
  * [Latest Epoch](#Latest-Epoch)
  * [Latest Epoch Protocol Parameters](#Latest-Epoch-Protocol-Parameters)
  * [Specific Epoch](#Specific-Epoch)
  * [Epochs History](#Epochs-History)
- [Pool](#Pool)
  * [List Of Stake Pools](#List-Of-Stake-Pools)
  * [Specific Stake Pool Informations](#Specific-Stake-Pool-Informations)
  * [Epochs History](#Epochs-History)
  * [Stake Pool History](#Stake-Pool-History)
- [Assets](#Assets)
  * [Assets List](#Assets-List)
  * [Specific Asset](#Specific-Asset)
  * [Asset History](#Asset-History)
  * [Assets Of A Specific Policy](#Assets-Of-A-Specific-Policy)
  * [Get Assets Informations](#Get-Assets-Informations)
- [Transactions](#Transactions)
  * [Specific Transaction](#Specific-Transaction)
  * [Transaction UTXOs](#Transaction-UTXOs)
  * [Transaction Stake Addresses Certificates](#Transaction-Stake-Addresses-Certificates)
  * [Transaction delegation certificates](#Transaction-delegation-certificates)
  * [Transaction Withdrawal](#Transaction-Withdrawal)
  * [Transaction MIRs](#Transaction-MIRs)
  * [Transaction Stake Pool Registration And Update Certificates](#Transaction-Stake-Pool-Registration-And-Update-Certificates)
  * [Transaction Stake Pool Cetirement Certificates](#Transaction-Stake-Pool-Retirement-Certificates)
  * [Transaction Metadata](#Transaction-Metadata)
  * [Transaction Metadata in CBOR](#Transaction-Metadata-In-CBOR)
  * [Transaction Redeemers](#Transaction-Redeemers)
- [Scripts](#Scripts)
  * [List of scripts](#Scripts)
  * [Specific Script](#Specific-Script)
  * [Redeemers Of A Specific Script](#Redeemers-Of-A-Specific-Script)
- [Examples](#Examples)
  * [Stake Rewards Analysis](https://github.com/djessy-atta/py-cardano-explorer/blob/main/src/notebooks/stake_rewards_analysis.ipynb)
  * [CNFT Analysis](https://github.com/djessy-atta/py-cardano-explorer/blob/main/src/notebooks/cnft_analysis.ipynb)
- [Developing](#Developing)
- [Credit](#Credit)
- [Donation](#Donate)
- [Disclaimer](#Disclaimer)

<br />

## Install


```python
pip install cardano_explorer
```

## Usage


```python
from cardano_explorer import blockfrost_api
```

## Api Key
If you have an API key, you can either set it as environment variable **BLOCKFROST_API_KEY** or set it manually. 

> You can quickly create your api key on [Blockfrost](https://blockfrost.io/#introduction).  
The free account allow you up to **50,000 requests** a day and **10 requests per second**,  which is more that enough.


```python
cardano_mainnet = blockfrost_api.Auth() # API Key is set in a env variable name BLOCKFROST_API_KEY
#or
cardano_mainnet = blockfrost_api.Auth(api_key=blockfrost_api_key)
```

## Using With Proxy


```python
proxies = {
 "http": "http://user:password@server:port",
 "https": "https://user:password@server:portt",
}

cardano_mainnet = blockfrost_api.Auth(proxies=proxies)
```

## Network
You can specify the cardano network with the class parameter **network**.


```python
cardano_mainnet = blockfrost_api.Auth() # mainnet by default
#or
cardano_mainnet = blockfrost_api.Auth(network='mainnet')
#or
cardano_mainnet = blockfrost_api.Auth(network='testnet')
```

## Network Informations

### Network Info
Return detailed about the network.


```python
cardano_mainnet.network_info()
```




    {'supply': {'max': '45000000000000000',
      'total': '33250650235236357',
      'circulating': '32921356877345090',
      'locked': '14342846495117',
      'treasury': '643991464810237',
      'reserves': '11749349764763643'},
     'stake': {'live': '23461249229811191', 'active': '23411124422164299'}}



## Stake

### Stake Informations
Obtain information about a specific stake account.


```python
cardano_mainnet.stake_informations(stake_address)
```




    {'stake_address': 'stake1uyttshgm6jtejckv48tll58hfw3fg2ffrcc4d5qvcc4yc7q9jsalf',
     'active': True,
     'active_epoch': 271,
     'controlled_amount': '3015398847',
     'rewards_sum': '33831666',
     'withdrawals_sum': '21239707',
     'reserves_sum': '97317',
     'treasury_sum': '0',
     'withdrawable_amount': '12591959',
     'pool_id': 'pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288ys5kumqce5'}



### Stake Reward History 
Obtain information about the reward history of a specific account.


```python
cardano_mainnet.stake_reward_history(stake_address, 
                                     data_order='asc', # Optional: Data order (default: Ascending)
                                     nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                     pandas=True) # Optional: Return a pandas dataframe
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>epoch</th>
      <th>amount</th>
      <th>pool_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>273</td>
      <td>587159</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>274</td>
      <td>715853</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>275</td>
      <td>902199</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>276</td>
      <td>824733</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>277</td>
      <td>1056705</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
  </tbody>
</table>
</div>



### Stake Rewards History Analysis
Add extra informations to the stake reward history.


```python
cardano_mainnet.stake_rewards_corr(stake_address,
                                   pandas=True) # Optional: Return a pandas dataframe 
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>epoch</th>
      <th>rewards_amount</th>
      <th>stake_amount</th>
      <th>pool_id</th>
      <th>epoch_start_time</th>
      <th>epoch_end_time</th>
      <th>epoch_first_block_time</th>
      <th>epoch_last_block_time</th>
      <th>epoch_block_count</th>
      <th>epoch_tx_count</th>
      <th>epoch_output</th>
      <th>epoch_fees</th>
      <th>epoch_active_stake</th>
      <th>stake_pool_blocks</th>
      <th>stake_pool_active_stake</th>
      <th>stake_pool_active_size</th>
      <th>stake_pool_delegators_count</th>
      <th>stake_pool_rewards</th>
      <th>stake_pool_fees</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>15</th>
      <td>288</td>
      <td>1768631</td>
      <td>2866605326</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
      <td>1630619091</td>
      <td>1631051091</td>
      <td>1630619101</td>
      <td>1631051088</td>
      <td>21136</td>
      <td>475383</td>
      <td>120564869080762073</td>
      <td>99992854778</td>
      <td>23136223153988390</td>
      <td>49</td>
      <td>55449417952886</td>
      <td>0.002397</td>
      <td>1439</td>
      <td>34863643156</td>
      <td>685236431</td>
    </tr>
    <tr>
      <th>16</th>
      <td>289</td>
      <td>2390373</td>
      <td>2868437494</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
      <td>1631051091</td>
      <td>1631483091</td>
      <td>1631051131</td>
      <td>1631483087</td>
      <td>21195</td>
      <td>501443</td>
      <td>30450853050129419</td>
      <td>105082493097</td>
      <td>23311196777534712</td>
      <td>66</td>
      <td>55724573270655</td>
      <td>0.002390</td>
      <td>1443</td>
      <td>47200199605</td>
      <td>808601996</td>
    </tr>
    <tr>
      <th>17</th>
      <td>290</td>
      <td>1878132</td>
      <td>3002707784</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
      <td>1631483091</td>
      <td>1631915091</td>
      <td>1631483266</td>
      <td>1631915089</td>
      <td>21320</td>
      <td>423156</td>
      <td>28653067841498377</td>
      <td>88193252097</td>
      <td>23253494675755279</td>
      <td>49</td>
      <td>54675837934319</td>
      <td>0.002351</td>
      <td>1440</td>
      <td>34877628423</td>
      <td>685376284</td>
    </tr>
    <tr>
      <th>18</th>
      <td>291</td>
      <td>2059700</td>
      <td>3004575519</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
      <td>1631915091</td>
      <td>1632347091</td>
      <td>1631915193</td>
      <td>1632347076</td>
      <td>21261</td>
      <td>415399</td>
      <td>27614827533993432</td>
      <td>88508486990</td>
      <td>23219858534473043</td>
      <td>54</td>
      <td>54806809508971</td>
      <td>0.002360</td>
      <td>1451</td>
      <td>38286415852</td>
      <td>719464158</td>
    </tr>
    <tr>
      <th>19</th>
      <td>292</td>
      <td>2173115</td>
      <td>3006965892</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
      <td>1632347091</td>
      <td>1632779091</td>
      <td>1632347163</td>
      <td>1632779076</td>
      <td>21264</td>
      <td>448774</td>
      <td>19991338650818976</td>
      <td>94575307119</td>
      <td>23325839206372436</td>
      <td>60</td>
      <td>57943587612745</td>
      <td>0.002484</td>
      <td>1451</td>
      <td>42628197872</td>
      <td>762881978</td>
    </tr>
  </tbody>
</table>
</div>



### Stake Amount History 
Obtain information about the history of a specific account.


```python
cardano_mainnet.stake_amount_history(stake_address, 
                                     data_order='asc', # Optional: Data order (default: Ascending)
                                     nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                     pandas=True) # Optional: Return a pandas dataframe
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>active_epoch</th>
      <th>amount</th>
      <th>pool_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>273</td>
      <td>998824863</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>274</td>
      <td>998824863</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>275</td>
      <td>1618824863</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>276</td>
      <td>1619412022</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>277</td>
      <td>1620127875</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
  </tbody>
</table>
</div>



### Stake Delegation History
Obtain information about the delegation of a specific account.


```python
cardano_mainnet.stake_delegation(stake_address, 
                                 data_order='asc', # Optional: Data order (default: Ascending)
                                 nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                 pandas=True) # Optional: Return a pandas dataframe
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>active_epoch</th>
      <th>tx_hash</th>
      <th>amount</th>
      <th>pool_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>273</td>
      <td>97a774aa60a2926c9949bfe1edf1dcc2f2297d36633e14...</td>
      <td>497824863</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
    </tr>
  </tbody>
</table>
</div>



### Stake Registrations And Deregistrations History
Obtain information about the registrations and deregistrations of a specific account.


```python
cardano_mainnet.stake_registration_deregistrations(stake_address, 
                                                   data_order='asc', # Optional: Data order (default: Ascending)
                                                   nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                                   pandas=True) # Optional: Return a pandas dataframe
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tx_hash</th>
      <th>action</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>97a774aa60a2926c9949bfe1edf1dcc2f2297d36633e14...</td>
      <td>registered</td>
    </tr>
  </tbody>
</table>
</div>



### Stake Withdrawal History
Obtain information about the withdrawals of a specific account.


```python
cardano_mainnet.stake_withdrawal_history(stake_address, 
                                         data_order='asc', # Optional: Data order (default: Ascending)
                                         nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                         pandas=True) # Optional: Return a pandas dataframe
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tx_hash</th>
      <th>amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>80b09b61d2da86f5847d0b9a5f72d32224fcd7e1aa1716...</td>
      <td>21239707</td>
    </tr>
  </tbody>
</table>
</div>



### Stake MIR History
Obtain information about the MIRs of a specific account.


```python
cardano_mainnet.stake_mir_history(stake_address, 
                                  data_order='asc', # Optional: Data order (default: Ascending)
                                  nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                  pandas=True) # Optional: Return a pandas dataframe
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tx_hash</th>
      <th>amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>c041e475d161444a6a8ca9005ef3deb36ebd579c347d90...</td>
      <td>74456</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9ede69b0ebd0903b1cc6a914a79fabd9a5d6dd94e8c110...</td>
      <td>22861</td>
    </tr>
  </tbody>
</table>
</div>



### Stake Associated Addresses
Obtain information about the MIRs of a specific account.


```python
cardano_mainnet.stake_associated_addresses(stake_address, 
                                           data_order='asc', # Optional: Data order (default: Ascending)
                                           nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                           pandas=True) # Optional: Return a pandas dataframe 
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>address</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>addr1qx96yn08e5u7hthawh63ss6269dkzxekq85elrthw...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>addr1q9u0kfvd57parl03j8v9fz52xqz8yjkcu47lcy8hw...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>addr1q8m6tn3edl333c8yzms8dzrkkckm0vn0dkvq436au...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>addr1q9py3k58fmyu896charn6mey8c5f22uq830m4udsy...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>addr1q8mk7kft30hwmj2yttltm8j5f4ccuguxr9z3werwm...</td>
    </tr>
  </tbody>
</table>
</div>



### Stake Assets Associated Addresses
Obtain information about assets associated with addresses of a specific account.</blockquote>


```python
cardano_mainnet.stake_assets_associated_addresses(stake_address, 
                                                  data_order='asc', # Optional: Data order (default: Ascending)
                                                  nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                                  pandas=True) # Optional: Return a pandas dataframe 
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>unit</th>
      <th>quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



# Address

### Specific Address
Obtain information about a specific address.


```python
cardano_mainnet.address_info(address)
```




    {'address': 'addr1q8z24xgrlj3m2qjh2vxyqg2fh33y3tegufkll5c4lu8u35gkhpw3h4yhn93ve2whllg0wjazjs5jj8332mgqe332f3uq8m7m6h',
     'amount': [{'unit': 'lovelace', 'quantity': '350000000'}],
     'stake_address': 'stake1uyttshgm6jtejckv48tll58hfw3fg2ffrcc4d5qvcc4yc7q9jsalf',
     'type': 'shelley'}



### Address Details
Obtain details about an address.


```python
cardano_mainnet.address_details(address)
```




    {'address': 'addr1q8z24xgrlj3m2qjh2vxyqg2fh33y3tegufkll5c4lu8u35gkhpw3h4yhn93ve2whllg0wjazjs5jj8332mgqe332f3uq8m7m6h',
     'received_sum': [{'unit': 'lovelace', 'quantity': '350000000'}],
     'sent_sum': [{'unit': 'lovelace', 'quantity': '0'}],
     'tx_count': 1}



### Address UTXOs
UTXOs of the address.


```python
cardano_mainnet.address_utxo(address,
                             pandas=True) # Optional: Return a pandas dataframe 
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tx_hash</th>
      <th>tx_index</th>
      <th>output_index</th>
      <th>amount</th>
      <th>block</th>
      <th>data_hash</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>996ff0a57282ef943ecdbc263cf9c41c178d65587d70d9...</td>
      <td>4</td>
      <td>4</td>
      <td>[{'unit': 'lovelace', 'quantity': '350000000'}]</td>
      <td>73768f4ca2a0c96611a1fbd7f53a3b1b573fb0371012e5...</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>



### Address Transactions
Transactions on the address.


```python
cardano_mainnet.address_transaction(address, 
                                    pandas=True) # Optional: Return a pandas dataframe 
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tx_hash</th>
      <th>tx_index</th>
      <th>block_height</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>996ff0a57282ef943ecdbc263cf9c41c178d65587d70d9...</td>
      <td>45</td>
      <td>6095572</td>
    </tr>
  </tbody>
</table>
</div>



## Epoch

### Latest Epoch
Obtain the information about the latest epoch.


```python
cardano_mainnet.latest_epoch()
```




    {'epoch': 288,
     'start_time': 1630619091,
     'end_time': 1631051091,
     'first_block_time': 1630619101,
     'last_block_time': 1630695809,
     'block_count': 3867,
     'tx_count': 77200,
     'output': '41529702474109934',
     'fees': '16021622015',
     'active_stake': '23136223153988390'}



### Latest Epoch Protocol Parameters
Return the protocol parameters for the latest epoch.


```python
cardano_mainnet.latest_epoch_protocol_parameters()
```




    {'epoch': 288,
     'min_fee_a': 44,
     'min_fee_b': 155381,
     'max_block_size': 65536,
     'max_tx_size': 16384,
     'max_block_header_size': 1100,
     'key_deposit': '2000000',
     'pool_deposit': '500000000',
     'e_max': 18,
     'n_opt': 500,
     'a0': 0.3,
     'rho': 0.003,
     'tau': 0.2,
     'decentralisation_param': 0,
     'extra_entropy': None,
     'protocol_major_ver': 4,
     'protocol_minor_ver': 0,
     'min_utxo': '1000000',
     'min_pool_cost': '340000000',
     'nonce': 'bf3b52ab86e152b392cbf095c1d0f07aaeda956eecfdb44b09bcb85a0ecae36a'}



### Specific Epoch
Obtain informations about a specific epoch.


```python
cardano_mainnet.specific_epoch(287)
```




    {'epoch': 287,
     'start_time': 1630187091,
     'end_time': 1630619091,
     'first_block_time': 1630187230,
     'last_block_time': 1630619085,
     'block_count': 21065,
     'tx_count': 401343,
     'output': '74754307451589173',
     'fees': '86536781869',
     'active_stake': '23041097075076811'}



### Epochs History
Obtain informations about sevrals epochs.


```python
cardano_mainnet.epochs_history([270, 271, 272],
                               pandas=True) # Optional: Return a pandas dataframe 
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>epoch</th>
      <th>start_time</th>
      <th>end_time</th>
      <th>first_block_time</th>
      <th>last_block_time</th>
      <th>block_count</th>
      <th>tx_count</th>
      <th>output</th>
      <th>fees</th>
      <th>active_stake</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>270</td>
      <td>1622843091</td>
      <td>1623275091</td>
      <td>1622843183</td>
      <td>1623275038</td>
      <td>21395</td>
      <td>174334</td>
      <td>12213404538685056</td>
      <td>36489177917</td>
      <td>22893778548073522</td>
    </tr>
    <tr>
      <th>1</th>
      <td>271</td>
      <td>1623275091</td>
      <td>1623707091</td>
      <td>1623275098</td>
      <td>1623707059</td>
      <td>21410</td>
      <td>145244</td>
      <td>12686700012872148</td>
      <td>30802442909</td>
      <td>22970909569111347</td>
    </tr>
    <tr>
      <th>2</th>
      <td>272</td>
      <td>1623707091</td>
      <td>1624139091</td>
      <td>1623707123</td>
      <td>1624139087</td>
      <td>21499</td>
      <td>135373</td>
      <td>10640794327820158</td>
      <td>29593210504</td>
      <td>23020000415780615</td>
    </tr>
  </tbody>
</table>
</div>



# Pool

### List Of Stake Pools
List of registered stake pools.


```python
cardano_mainnet.registered_polls(nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                 pandas=True) # Optional: Return a pandas dataframe 
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>registered_polls_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>pool1z5uqdk7dzdxaae5633fqfcu2eqzy3a3rgtuvy087f...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pool1pu5jlj4q9w9jlxeu370a3c9myx47md5j5m2str0na...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pool1c8k78ny3xvsfgenhf4yzvpzwgzxmz0t0um0h2xnn2...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>pool1q80jjs53w0fx836n8g38gtdwr8ck5zre3da90peux...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>pool1ddskftmsscw92d7vnj89pldwx5feegkgcmamgt5t0...</td>
    </tr>
  </tbody>
</table>
</div>



### Specific Stake Pool Informations
Pool informations.


```python
cardano_mainnet.pool_informations(pool_id)
```




    {'pool_id': 'pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288ys5kumqce5',
     'hex': 'cdae4a1a08974113e77ea332cb1da97d9e3fca5cf797f9394739214b',
     'vrf_key': '5517fbeb4c6a5a613835808de183345eaf85ab0e251210e493e088afa41d9ab0',
     'blocks_minted': 3454,
     'live_stake': '63777749141588',
     'live_size': 0.002722243022656593,
     'live_saturation': 0.9701750363479381,
     'live_delegators': 1411,
     'active_stake': '880520384',
     'active_size': 8.842681417401523e-05,
     'declared_pledge': '200000000000',
     'live_pledge': '205263294816',
     'margin_cost': 0.01,
     'fixed_cost': '340000000',
     'reward_account': 'stake1u8uzevd539lxn40jt60g72a649zdphe9e8hrye4nf5jv0js9uzhzg',
     'owners': ['stake1u9qsgte62jau0qu6kjy8zch8aynt55gql6jsxe05464n99gsqd7ra',
      'stake1u8uzevd539lxn40jt60g72a649zdphe9e8hrye4nf5jv0js9uzhzg'],
     'registration': ['b1bfffc26b6210ced9cc679781922e8b1ac70a2f7719523528639da4ab7f2d88',
      'be5b798897f5b83e5bf562df6fc68a94d5528acc80ab8e999ce866aa63a4d06a',
      '0f4781efd649f91e37847cb2699a8a41632ee94df1465e255577772f362339bf',
      '630c7195fdc1c5c14bb12c460059c5adb11b3cd6d3e576628aee0a8338f1b6ad',
      '119fe23a35e0ddcbb5778f17ad2371228a53b5ced037c12083a0c77b5711e1d4',
      'f1fe58c30ec7f5193476694fafc46dcdb11c3408e114e8fa2a95425243907ed4',
      '09c2c3d34de116365c9cf9a6e75f45856013388d962dbd5584c27b7d0bb36eed'],
     'retirement': []}



### Stake Pool History

History of stake pool over epochs.


```python
cardano_mainnet.stake_pool_history(pool_id,
                                   pandas=True).tail() # Optional: Return a pandas dataframe 
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>epoch</th>
      <th>blocks</th>
      <th>active_stake</th>
      <th>active_size</th>
      <th>delegators_count</th>
      <th>rewards</th>
      <th>fees</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>81</th>
      <td>291</td>
      <td>54</td>
      <td>54806809508971</td>
      <td>0.002360</td>
      <td>1451</td>
      <td>38286415852</td>
      <td>719464158</td>
    </tr>
    <tr>
      <th>82</th>
      <td>292</td>
      <td>60</td>
      <td>57943587612745</td>
      <td>0.002484</td>
      <td>1451</td>
      <td>42628197872</td>
      <td>762881978</td>
    </tr>
    <tr>
      <th>83</th>
      <td>293</td>
      <td>70</td>
      <td>63400551099817</td>
      <td>0.002710</td>
      <td>1440</td>
      <td>49751668542</td>
      <td>834116685</td>
    </tr>
    <tr>
      <th>84</th>
      <td>294</td>
      <td>49</td>
      <td>62772203979076</td>
      <td>0.002685</td>
      <td>1431</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>85</th>
      <td>295</td>
      <td>34</td>
      <td>63837104114656</td>
      <td>0.002727</td>
      <td>1416</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



# Assets

### Assets List
List of assets.


```python
cardano_mainnet.assets(data_order='asc', # Optional: Data order (default: Ascending)
                       nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                       pandas=True).head() # Optional: Return a pandas dataframe 
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>asset</th>
      <th>quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>00000002df633853f6a47465c9496721d2d5b1291b8398...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3a9241cd79895e3a8d65261b40077d4437ce71e9d7c8c6...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>02f68378e37af4545d027d0a9fa5581ac682897a3fc1f6...</td>
      <td>1000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>e8e62d329e73190190c3e323fb5c9fb98ee55f0676332b...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ac3f4224723e2ed9d166478662f6e48bae9ddf0fc5ee58...</td>
      <td>10000000</td>
    </tr>
  </tbody>
</table>
</div>



### Specific Asset
Information about a specific asset.


```python
cardano_mainnet.specific_asset(policy_id+asset_name)
```




    {'asset': '40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c28262fab21728436c61794e6174696f6e33393836',
     'policy_id': '40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c28262fab21728',
     'asset_name': '436c61794e6174696f6e33393836',
     'fingerprint': 'asset1ay3atwzy3hrdnn74v05jusgsycl344nquyq9nq',
     'quantity': '1',
     'initial_mint_tx_hash': '117f97ccf6e98a16697e7cc205daf2d0bfe83d849a63df2f40d10bef235848e7',
     'mint_or_burn_count': 1,
     'onchain_metadata': {'name': 'Clay Nation #3986',
      'image': 'ipfs://QmYREMX1uTQAFScJD4Xv5tUPnWimKyLzBTBFLv1oCyzMj2',
      'body': 'Brown Clay',
      'eyes': 'Big Eyes',
      'brows': 'Normal Eyebrows',
      'mouth': 'Normal Mouth',
      'Project': 'Clay Nation by Clay Mates',
      'clothes': 'Tshirt Green',
      'background': 'Cyan',
      'accessories': 'Flower Necklace',
      'hats and hair': 'Fringe'},
     'metadata': None}



### Asset History
History of a specific asset.


```python
cardano_mainnet.asset_history(policy_id+asset_name,
                               data_order='asc', # Optional: Data order (default: Ascending)
                               nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                               pandas=True) # Optional: Return a pandas dataframe
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tx_hash</th>
      <th>action</th>
      <th>amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>117f97ccf6e98a16697e7cc205daf2d0bfe83d849a63df...</td>
      <td>minted</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Asset Transactions
List of a specific asset transactions.


```python
cardano_mainnet.asset_addresses(policy_id+asset_name,
                                data_order='asc', # Optional: Data order (default: Ascending)
                                nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                pandas=True) # Optional: Return a pandas dataframe 
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>address</th>
      <th>quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>addr1q9vzk47zqxj54kew38j735n92mncnyhq57uekgn4w...</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Assets Of A Specific Policy

List of assets mint under a specific policy


```python
cardano_mainnet.assets_policy(policy_id,
                              data_order='asc', # Optional: Data order (default: Ascending)
                              nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                              pandas=True) # Optional: Return a pandas dataframe 
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>asset</th>
      <th>quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Get Assets Informations 
Get informations about the assests mint under a specific policy.  
Look [here]() for some examples on how to analyze a CNFT project


```python
assets_info = cardano_mainnet.assets_policy_info(policy_id, # Policy ID
                                                 nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                                                 pandas=True) # Optional: Return a pandas dataframe 
```

<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>asset</th>
      <th>policy_id</th>
      <th>asset_name</th>
      <th>fingerprint</th>
      <th>quantity</th>
      <th>initial_mint_tx_hash</th>
      <th>mint_or_burn_count</th>
      <th>onchain_metadata</th>
      <th>metadata</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c282...</td>
      <td>436c61794e6174696f6e37383939</td>
      <td>asset1xkngd3y2njd3dzhfg25rtfp66gyvke6skqftxc</td>
      <td>1</td>
      <td>d7e089dce7c170f1af519fab710f9ed5d4d8680978035d...</td>
      <td>1</td>
      <td>{'name': 'Clay Nation #7899', 'image': 'ipfs:/...</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>



# Transactions

### Specific Transaction

Return content of the requested transaction.


```python
cardano_mainnet.specific_tx(tx_hash)
```




    {'hash': '117f97ccf6e98a16697e7cc205daf2d0bfe83d849a63df2f40d10bef235848e7',
     'block': 'ff4399874973f4eda1fe3e57be7bd47a02b610188d41993abac97605a2e7af07',
     'block_height': 6222808,
     'slot': 39646908,
     'index': 1,
     'output_amount': [{'unit': 'lovelace', 'quantity': '39793491'},
      {'unit': '40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c28262fab21728436c61794e6174696f6e33393836',
       'quantity': '1'}],
     'fees': '206509',
     'deposit': '0',
     'size': 924,
     'invalid_before': None,
     'invalid_hereafter': '50000000',
     'utxo_count': 3,
     'withdrawal_count': 0,
     'mir_cert_count': 0,
     'delegation_count': 0,
     'stake_cert_count': 0,
     'pool_update_count': 0,
     'pool_retire_count': 0,
     'asset_mint_or_burn_count': 1,
     'redeemer_count': 0}



### Transaction UTXOs

Return the inputs and UTXOs of the specific transaction.


```python
cardano_mainnet.tx_utxos(tx_hash)
```




    {'hash': '117f97ccf6e98a16697e7cc205daf2d0bfe83d849a63df2f40d10bef235848e7',
     'inputs': [{'address': 'addr1vytxp3vg7gtn27zh8fa8dz677wpd2hvdz3fzzxmtgfhzmfg7d6z6g',
       'amount': [{'unit': 'lovelace', 'quantity': '40000000'}],
       'tx_hash': 'c6b37283f5051cd67338b35867105b0d5f0609430ca31b550c1068ded23a19ed',
       'output_index': 0,
       'collateral': False,
       'data_hash': None}],
     'outputs': [{'address': 'addr1qx0y89lj0tc5uzrdpq565ymcuuctw9w6kzsqrsgjfeg7hfw7rv0m0sssgyy0xaqn0h3fm8szh4hnz9myue7j3djpjf6q9rvj6c',
       'amount': [{'unit': 'lovelace', 'quantity': '37793491'}],
       'output_index': 0,
       'data_hash': None},
      {'address': 'addr1q9ylsfx9cl8npeajmzn82k2qlt6qks6mzefmdu9fh255n90qnc7ytmfse2feyp66wqajvappey935tefg5lrxxfjfcnsuhkt7p',
       'amount': [{'unit': 'lovelace', 'quantity': '2000000'},
        {'unit': '40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c28262fab21728436c61794e6174696f6e33393836',
         'quantity': '1'}],
       'output_index': 1,
       'data_hash': None}]}



### Transaction Stake Addresses Certificates

Obtain information about (de)registration of stake addresses within a transaction.


```python
cardano_mainnet.tx_stake_address_cert(stake_tx_hash,
                                      pandas=True) # Optional: Return a pandas dataframe 
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cert_index</th>
      <th>address</th>
      <th>registration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>stake1uyttshgm6jtejckv48tll58hfw3fg2ffrcc4d5qv...</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



### Transaction Delegation Certificates

Obtain information about delegation certificates of a specific transaction.


```python
cardano_mainnet.tx_delegation_cert(stake_tx_hash,
                                   pandas=True) # Optional: Return a pandas dataframe 
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>cert_index</th>
      <th>address</th>
      <th>pool_id</th>
      <th>active_epoch</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>stake1uyttshgm6jtejckv48tll58hfw3fg2ffrcc4d5qv...</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
      <td>273</td>
    </tr>
  </tbody>
</table>
</div>



### Transaction Withdrawal

Obtain information about withdrawals of a specific transaction.


```python
cardano_mainnet.tx_withdrawal_url(stake_withdrawal_tx_hash,
                                  pandas=True) # Optional: Return a pandas dataframe 
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>address</th>
      <th>amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>stake1uyttshgm6jtejckv48tll58hfw3fg2ffrcc4d5qv...</td>
      <td>21239707</td>
    </tr>
  </tbody>
</table>
</div>



### Transaction MIRs

Obtain information about Move Instantaneous Rewards (MIRs) of a specific transaction.


```python
cardano_mainnet.tx_transaction_mirs(stake_mir_tx_hash,
                                    pandas=True) # Optional: Return a pandas dataframe
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pot</th>
      <th>cert_index</th>
      <th>address</th>
      <th>amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>reserve</td>
      <td>0</td>
      <td>stake1uytqd6u9nv0tme27mew3tfcyysdz38e3v940xmph...</td>
      <td>20345</td>
    </tr>
    <tr>
      <th>1</th>
      <td>reserve</td>
      <td>0</td>
      <td>stake1uytpqufg9zkmj6lw4t97gtwzqnl5fqfrtyxvyrt3...</td>
      <td>102354</td>
    </tr>
    <tr>
      <th>2</th>
      <td>reserve</td>
      <td>0</td>
      <td>stake1uytpf8fksuqszgacpfhgdpvpa2phu0r72hyjat9m...</td>
      <td>969473</td>
    </tr>
    <tr>
      <th>3</th>
      <td>reserve</td>
      <td>0</td>
      <td>stake1uytpsyyj8pz4jmk7psl3z9hclnga05xgvxkh6p70...</td>
      <td>602920</td>
    </tr>
    <tr>
      <th>4</th>
      <td>reserve</td>
      <td>0</td>
      <td>stake1uytphp0lmjuzagh4x45favh3760dljqxcmgmpyyp...</td>
      <td>57335</td>
    </tr>
  </tbody>
</table>
</div>



### Transaction Stake Pool Registration And Update Certificates

Obtain information about stake pool registration and update certificates of a specific transaction.


```python
cardano_mainnet.tx_stake_pool_update(stake_pool_registration_tx_hash,
                                     pandas=True) # Optional: Return a pandas dataframe
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cert_index</th>
      <th>pool_id</th>
      <th>vrf_key</th>
      <th>pledge</th>
      <th>margin_cost</th>
      <th>fixed_cost</th>
      <th>reward_account</th>
      <th>owners</th>
      <th>metadata</th>
      <th>relays</th>
      <th>active_epoch</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>pool1ekhy5xsgjaq38em75vevk8df0k0rljju77tljw288...</td>
      <td>5517fbeb4c6a5a613835808de183345eaf85ab0e251210...</td>
      <td>90000000000</td>
      <td>0.01</td>
      <td>380000000</td>
      <td>stake1u9qsgte62jau0qu6kjy8zch8aynt55gql6jsxe05...</td>
      <td>[stake1u9qsgte62jau0qu6kjy8zch8aynt55gql6jsxe0...</td>
      <td>{'url': 'https://meta.staking.outofbits.com/so...</td>
      <td>[{'ipv4': None, 'ipv6': None, 'dns': 'toki.rel...</td>
      <td>210</td>
    </tr>
  </tbody>
</table>
</div>



### Transaction Stake Pool Retirement Certificates

Obtain information about stake pool retirements within a specific transaction.


```python
cardano_mainnet.tx_stake_pool_retirement_cert(tx_hash,
                                              pandas=True) # Optional: Return a pandas dataframe
```


```python
import pandas as pd
pd.DataFrame.from_dict([{
"cert_index": 0,
"pool_id": "pool1ekly5isgkaq38em75vevk0df0k0rljju77tljw288ys5kumqce5",
"retiring_epoch": 280
}])
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cert_index</th>
      <th>pool_id</th>
      <th>retiring_epoch</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>pool1ekly5isgkaq38em75vevk0df0k0rljju77tljw288...</td>
      <td>280</td>
    </tr>
  </tbody>
</table>
</div>



### Transaction Metadata

Obtain the transaction metadata.


```python
cardano_mainnet.tx_metadata(tx_hash, 
                            pandas=True) # Optional: Return a pandas dataframe
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>label</th>
      <th>json_metadata</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>721</td>
      <td>{'40fa2aa67258b4ce7b5782f74831d46a84c59a0ff0c2...</td>
    </tr>
  </tbody>
</table>
</div>



### Transaction Metadata In CBOR

Obtain the transaction metadata in CBOR.


```python
cardano_mainnet.tx_cbor_metadata(tx_hash,
                                 pandas=True) # Optional: Return a pandas dataframe
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>label</th>
      <th>cbor_metadata</th>
      <th>metadata</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>721</td>
      <td>\xa11902d1a17838343066613261613637323538623463...</td>
      <td>a11902d1a1783834306661326161363732353862346365...</td>
    </tr>
  </tbody>
</table>
</div>



### Transaction Redeemers

Obtain the transaction redeemers of a script.


```python
cardano_mainnet.tx_redeemers(script_redeemer_tx_hash,
                             pandas=True)# Optional: Return a pandas dataframe
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tx_index</th>
      <th>purpose</th>
      <th>unit_mem</th>
      <th>unit_steps</th>
      <th>fee</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>spend</td>
      <td>8879521</td>
      <td>2890961166</td>
      <td>2899840687</td>
    </tr>
  </tbody>
</table>
</div>



# Scripts

### List Of Sripts

Obtain the list of scripts.


```python
cardano_mainnet.scripts_list(data_order='asc', # Optional: Data order (default: Ascending)
                             nb_of_results=100, # Optional: Return max 100 results at the time (default: None), None for get all the data available.
                             pandas=True) # Optional: Return a pandas dataframe)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>script_hash</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>f55dfaa24ac08874405206588859ec2804b722a51eb716...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1fa88319dd2d0883c1a958d26da1d358444ca95a7eef6d...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4f590a3d80ae0312bad0b64d540c3ff5080e77250e9dbf...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>cc7888851f0f5aa64c136e0c8fb251e9702f3f6c9efcf3...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>81e9ffa364de993fbf2034f6db139adfd65eb69669b361...</td>
    </tr>
  </tbody>
</table>
</div>



### Specific Script

Information about a specific script.


```python
cardano_mainnet.specific_script(script_tx_hash)
```




    {'script_hash': 'cc7888851f0f5aa64c136e0c8fb251e9702f3f6c9efcf3a60a54f419',
     'type': 'plutus',
     'serialised_size': 3046}



### Redeemers Of A Specific Script

List of redeemers of a specific script


```python
cardano_mainnet.redeem_specific_script(script_hash)
```




    {'tx_hash': {0: 'e9d20746cec2d506a5ae201adbfec13ef20279b689f0612cc3802274ce4da2ce'},
     'tx_index': {0: 0},
     'purpose': {0: 'mint'},
     'unit_mem': {0: '1106480'},
     'unit_steps': {0: '397329109'},
     'fee': {0: '398435589'}}



# Developing
Tests run assuming you have set the API key in the environment variable ***BLOCKFROST_API_KEY***, otherwise they will error.


```python
python setup.py pytest
```

# Credit
- [Blockfrost API](https://blockfrost.io/).

# Donate

If this wrapper has been useful to you, feel free to put a star or donate (ADA) at this address :blush:.

![wallet address](src/img/wallet_address_50x50.jpg)

Thank you.

# Disclaimer
The project is still under development, If you find bugs or want additional features, open an issue and/or create a pull request.
