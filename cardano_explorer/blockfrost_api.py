#!/usr/bin/env python

import os
import pandas as pd
from .blockfrost.config import *
from time import sleep
from tqdm import tqdm
from .blockfrost.urls import *
from .blockfrost.util import add_onchain_metadata
from typing import Union, Optional, List, Dict, Tuple
from .blockfrost.query import query_blockfrost, query_on_several_pages

class Auth:
    def __init__(self, network: str="mainnet", apiKey: str=None,  proxies: dict=None):
        self.network  = network
        self.api_key  = apiKey
        self.proxies  = proxies
         
    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        network = self._network 
        
        # If the api key is not specidied, look if she is configured in environement variable
        if not value:
            if "mainnet" in network  and os.getenv(bf_osenv_mainnet_apiKey) != None:
                self._api_key = os.getenv('BLOCKFROST_MAINNET_API_KEY')

            elif "testnet" in network and os.getenv(bf_osenv_testnet_apiKey) != None:
                self._api_key = os.getenv('BLOCKFROST_LEGACY_API_KEY')

            elif "preview" in network and os.getenv(bf_osenv_preview_apiKey) != None:
                self._api_key = os.getenv('BLOCKFROST_PREVIEW_API_KEY')

            elif "preprod" in network and os.getenv(bf_osenv_preprod_apiKey) != None:
                self._api_key = os.getenv('BLOCKFROST_PREPROD_API_KEY')

            else:
               ValueError(f"[ERROR] Your blockfrost api key for the {network} is not configured in your environement path. Create an environement variable name {network} or set it manually using the param 'api_key'")
        # Else, use the api key set manually
        else:
            self._api_key = value

    @property
    def network(self):
        "Get the network"
        return self._network

    @network.setter
    def network(self, value):
        "Set the network"
        if 'mainnet' in value:
            self._network = bf_url_cardano_mainnet
        elif 'testnet' in value:
            self._network = bf_url_cardano_legacy
        elif 'preprod' in value:
            self._network = bf_url_cardano_preprod
        elif 'preview' in value:
            self._network = bf_url_cardano_preview
        else:
            raise ValueError('{} is not a valid network'.format(value))

    @property
    def proxies(self):
        "Set proxies"
        return self._proxies

    @proxies.setter
    def proxies(self, value):
        "Set proxies"
        self._proxies = value
 
    def stake_informations(self, stake_address: str) -> dict:
        """
        Obtain informations about a stake account.
        
        :param stake_address: The stake addresse
        :return: Dictionary with the informations about a specific stake account
        """
        
        url_stake_info = self.network + bf_stake_url + stake_address
        
        response = query_blockfrost(url_stake_info, self.api_key, self.proxies)
        
        return response
                 
    def stake_reward_history(self, stake_address: str, data_order: str='asc', nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain the reward history.
        
        :param stake_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, number of results wanted. The api return 100 results at a time. None for return all the data
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the rewards history 
        """
        
        rewards_history_url = "{}{}{}".format(bf_stake_url,
                                              stake_address,
                                              bf_stake_rewards_url)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, rewards_history_url, self.proxies)
        
        #print('[INFO] Function stake_reward_history, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    def stake_amount_history(self, stake_address: str, data_order: str='asc', nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain the stake amount history.
        
        :param stake_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, the number of results wanted
        :param nb_of_results: Optional, number of results wanted. The api return 100 results at a time. None for return all the data
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the stake amount history
        """
        
        stake_amount_history_url = "{}{}{}".format(bf_stake_url,
                                                   stake_address,
                                                   bf_stake_amount_history_url)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, stake_amount_history_url, self.proxies)
        
        #print('[INFO] Function stake_amount_history, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response
         
    def stake_delegation(self, stake_address: str, data_order: str='asc', nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain information about the stake delegation.
        
        :param stake_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, number of results wanted. The api return 100 results at a time. None for return all the data
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the stake delegation history
        """
        
        stake_delegation_url = "{}{}{}".format(bf_stake_url,
                                               stake_address,
                                               bf_stake_delegation_url)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, stake_delegation_url, self.proxies)
        
        #('[INFO] Function stake_delegation, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    def stake_registration_deregistrations(self, stake_address: str, data_order: str='asc', nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain information about the stake registration et deregistrations.
        
        :param stake_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, number of results wanted. The api return 100 results at a time. None for return all the data
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the stake registration and deregistrations history
        """
        
        stake_registration_url = "{}{}{}".format(bf_stake_url,
                                                 stake_address,
                                                 bf_stake_registration_url)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, stake_registration_url, self.proxies)
        
        #print('[INFO] Function stake_registration_deregistrations, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    def stake_withdrawal_history(self, stake_address: str, data_order: str='asc', nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain information about the stake withdrawal history.
        
        :param stake_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, number of results wanted. The api return 100 results at a time. None for return all the data
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the stake withdrawal history 
        """
        
        stake_withdrawal_history_url = "{}{}{}".format(bf_stake_url,
                                                       stake_address,
                                                       bf_stake_withdrawal_history_url)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, stake_withdrawal_history_url, self.proxies)
        
        #print('[INFO] Function stake_withdrawal_history, {} API calls.'.format(count_api_calls))
        
        if pandas:
            return pd.DataFrame.from_dict(response)
        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    def stake_mir_history(self, stake_address: str, data_order: str='asc', nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain information about the stake mir history.
        
        :param stake_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, number of results wanted. The api return 100 results at a time. None for return all the data
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the stake mir history
        """
        
        stake_mir_history_url = "{}{}{}".format(bf_stake_url,
                                                stake_address,
                                                bf_stake_mir_history_url)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, stake_mir_history_url, self.proxies) 
        
        #print('[INFO] Function stake_mir_history, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    def stake_associated_addresses(self, stake_address: str, data_order: str='asc', nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain information about the stake associated addresses.
        
        :param stake_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, number of results wanted. The api return 100 results at a time. None for return all the data
        :pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the stake associated addresses or empty dictionary if the stake address have no stake ADA
        """
        
        stake_associated_addresses_url = "{}{}{}".format(bf_stake_url,
                                                         stake_address,
                                                         bf_associated_addresses_url)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, stake_associated_addresses_url, self.proxies)
        
        #print('[INFO] Function stake_associated_addresses, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    def stake_assets_associated_addresses(self, stake_address: str, data_order: str='asc', nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain information about the stake assets associated addresses.
        
        :param stake_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, number of results wanted. The api return 100 results at a time. None for return all the data
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the stake associated addresses or empty dictionary if the stake address have no stake ADA
        """
        
        stake_assets_associated_addresses_url = "{}{}{}".format(bf_stake_url,
                                                                stake_address,
                                                                bf_assets_associated_addresses_url)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, stake_assets_associated_addresses_url, self.proxies)
        
        #print('[INFO] Function stake_assets_associated_addresses, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    def address_info(self, address: str) -> dict:
        """
        Obtain informations about an address.
        
        :param stake_addresse: Address
        :return: Dictionary or DataFrame with the informations about the address
        
        """
        
        address_info_url = self.network + bf_address_url + address
        
        response = query_blockfrost(address_info_url, self.api_key, self.proxies)
        
        return response
    
    def address_details(self, address: str) -> dict:
        """
        Obtain details information about an address.
        
        :param stake_addresse: Address
        :return: Dictionary with the informations details about the address
        """
        
        address_details_url = self.network + bf_address_url + address + bf_address_details_url
        
        response = query_blockfrost(address_details_url, self.api_key, self.proxies)
        
        return response
    
    def address_utxo(self, address: str, pandas: bool=False) -> dict:
        """
        Obtain UTXO of the address.
        
        :param stake_addresse: Address
        :return: Dictionary with the informations details about the UTXO of an address
        """
        
        address_utxo_url = self.network + bf_address_url + address + bf_address_utxo_url
        
        response = query_blockfrost(address_utxo_url, self.api_key, self.proxies)
        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    def address_transaction(self, address: str, pandas: bool=False) -> dict:
        """
        Transactions on the address.
        
        :param stake_addresse: Address
        :return: Dictionary with the informations details about the address transaction
        """
        
        address_transaction_url = self.network + bf_address_url + address + bf_address_transaction_url
        
        response = query_blockfrost(address_transaction_url, self.api_key, self.proxies)
        
        return pd.DataFrame.from_dict(response) if pandas else response
    
    def network_info(self) -> dict:
        """Return detailed network information."""
        
        network_info_url = self.network + bf_network_informations_url
        
        response = query_blockfrost(network_info_url, self.api_key, self.proxies)
        
        return response
    
    def latest_epoch(self) -> dict:
        """Return the information about the latest, therefore current, epoch."""
        
        latest_epoch_url = self.network + bf_latest_epoch_url
        
        response = query_blockfrost(latest_epoch_url, self.api_key, self.proxies)
        
        return response
    
    def specific_epoch(self, epoch: int) -> dict:
        """
        Obtain information about a specific epocht.
        
        :param epoch: The number of the epoch
        :return: Dictionary with information about a specific epoch
        """
        
        # Check if the epoch is greater than 0
        assert(int(epoch) >= 0), "[ERROR] The number of epoch can't be negatif."
        
        specific_epoch_url = self.network + bf_epoch_url + str(epoch)
        
        response = query_blockfrost(specific_epoch_url, self.api_key, self.proxies)
        
        return response
    
    def latest_epoch_protocol_parameters(self) -> dict:
        """Return the protocol parameters for the latest epoch."""
        
        address_info_url = self.network + bf_latest_epoch_protocol_parameters_url
        
        response = query_blockfrost(address_info_url, self.api_key, self.proxies)
        
        return response
     
    def epochs_history(self, epochs: list, pandas: bool=False) -> Union[pd.DataFrame, dict]:            
        """
        Obtain history about the epochs.
        
        :param epochs: List of the epochs number
        :pandas: Optional, True for return a pandas dataframe
        :return: Dictionary or DataFrame of the epochs informations history
        """
        
        # Check if the parameter epochs is a list
        assert(isinstance(epochs, list)), "[ERROR] The parameter 'epochs' should be a list not ({})".format(type(epochs))
    
        epochs_history = []
        last_epoch = self.latest_epoch()['epoch']
        
        # Value to 1 because of the first call for get the last epoch
        count_api_calls = 1
   
        for epoch in epochs:
            
            # check if the epoch number is not inferior than O or greater than the last epoch.
            assert(epoch > 0), "[ERROR] The number of epoch ({}) can't be inferior than 0.".format(epoch)
            assert(epoch < last_epoch), "ERROR] The number of epoch can't be greater than the last epoch ({})".format(last_epoch)
        
            epochs_history.append(self.specific_epoch(epoch))
            count_api_calls += 1
               
        #print('[INFO] Function epochs_history, {} API calls.'.format(count_api_calls))
            
        return pd.DataFrame.from_dict(epochs_history) if pandas else epochs_history
    
    def registered_polls(self, data_order: str='asc', nb_of_results: int=100, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain the list of registered stake pools.
        
        :param reward_address: The stake address
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, Number of results wanted. The api return 100 results at a time (default: 100)
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the registered stake pools
        """
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, bf_polls_url, self.proxies)
        
        # Rename the column of the pool ID
        response['registered_polls_id'] = response.pop(0)
                  
        #print('[INFO] Function registered_polls, {} API calls.'.format(count_api_calls))
                        
        return pd.DataFrame.from_dict(response) if pandas else response
     
    def pool_informations(self, pool_id: str) -> dict: 
        """
        Obtain Pool information.
        
        :param pool_id: The id of the pool
        :return: Dictionary with the informations about a pool
        """
        
        pool_informations_url = self.network + bf_polls_url + pool_id
        response = query_blockfrost(pool_informations_url, self.api_key, self.proxies)
        
        return response
      
    def stake_pool_history(self, pool_id: str, data_order: str='asc', nb_of_results: int=100, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain history of stake pool parameters over epochs
        
        :param pool_id: The id of the pool
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, Number of results wanted. The api return 100 results at a time (default: 100)
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return dict: Dictionary or DataFrame of the history of stake pool parameters over epochs
        """
        
        param_stake_pool_history_url = "{}{}{}".format(bf_polls_url,
                                                       pool_id,
                                                       bf_param_stake_pool_history_url)
        
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, param_stake_pool_history_url, self.proxies)
        
        #print('[INFO] Function param_stake_pool_history, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response
 
    def stake_rewards_corr(self, stake_address: str, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Create a dataframe with explanatory variables of the stake rewards for each epochs.

        :param stake_address: Stake address
        :pandas: Optional, True for return a pandas dataframe
        :return: Dictionary or DataFrame about informations on the rewards history
        """

        # Get the rewards history
        df_rewards_hist = self.stake_reward_history(stake_address, pandas=True).rename({'amount': 'rewards_amount'}, axis=1)
        epoch_reward_list = df_rewards_hist['epoch'].tolist()
        pool_id = df_rewards_hist['pool_id'][0]

        # Get the stake amount history
        df_amount_hist = self.stake_amount_history(stake_address, pandas=True).rename({'amount': 'stake_amount'}, axis=1)

        # Get the pool informations
        df_stake_pool_hist = self.stake_pool_history(pool_id, pandas=True)
        # Replace the column names
        df_stake_pool_hist_col_name = {name:'stake_pool_{}'.format(name) for name in df_stake_pool_hist.columns.tolist()}
        df_stake_pool_hist = df_stake_pool_hist.rename(columns=df_stake_pool_hist_col_name)

        # Get the epochs information
        df_epochs_hist = self.epochs_history(epoch_reward_list, pandas=True)
        # Replace the column names
        df_epochs_hist_col_name = {name:'epoch_{}'.format(name) for name in df_epochs_hist.columns.tolist()}
        df_epochs_hist = df_epochs_hist.rename(columns=df_epochs_hist_col_name)

        # Concatenate the data into a unique dataframe
        df = df_rewards_hist[['epoch','rewards_amount']].join(df_amount_hist.set_index('active_epoch'), on='epoch')
        df = df.join(df_epochs_hist.set_index('epoch_epoch'), on='epoch')
        df = df.join(df_stake_pool_hist.set_index('stake_pool_epoch'), on='epoch')

        return df if pandas else df.to_dict()

    def assets(self, data_order: str='asc', nb_of_results: int=100, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        List of assets.
        
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, Number of results wanted. The api return 100 results at a time (default: 100)
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the assets
        """
        

        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, bf_assets_url, self.proxies)
        
        #print('[INFO] Function assets, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response

    def specific_asset(self, asset: str) -> dict: 
        """
        Obtain information about a specific asset.
        
        :param assets: Assets (Concatenation of the policy_id and hex-encoded asset_name)
        :return: Dictionary with the info about the asset
        """
        
        specific_asset_url = self.network + bf_assets_url + asset

        response = query_blockfrost(specific_asset_url, self.api_key, self.proxies)
        
        return response
 
    def asset_history(self, asset: str, data_order: str='asc', nb_of_results: int=100, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        Obtain the history of a specific asset.
        
        :param assets: Assets (Concatenation of the policy_id and hex-encoded asset_name)
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, Number of results wanted. The api return 100 results at a time (default: 100)
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the assets
        """
        
        assets_history_url = bf_assets_url + asset + bf_asset_history_url

        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, assets_history_url, self.proxies)
        
        #print('[INFO] Function asset_history, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response

    def asset_transactions(self, asset: str, data_order: str='asc', nb_of_results: int=100, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        List of a specific asset transactions.
        
        :param assets: Assets (Concatenation of the policy_id and hex-encoded asset_name)
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, Number of results wanted. The api return 100 results at a time (default: 100)
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the assets
        """
        
        assets_transactions_url = bf_assets_url + asset + bf_asset_transactions_url

        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, assets_transactions_url, self.proxies)
        
        #print('[INFO] Function asset_transactions, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response
     
    def asset_addresses(self, asset: str, data_order: str='asc', nb_of_results: int=100, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        List of a addresses containing a specific asset.
        
        :param assets: Assets (Concatenation of the policy_id and hex-encoded asset_name)
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, Number of results wanted. The api return 100 results at a time (default: 100)
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the assets
        """
        
        assets_addresses_url = bf_assets_url + asset + bf_asset_addresses_url
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, assets_addresses_url, self.proxies)
        
        #print('[INFO] Function asset_addresses, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response

    def assets_policy(self, policy_id: str, data_order: str='asc', nb_of_results: int=100, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        List of asset minted under a specific policy.
        
        :param policy_id: Policy ID of the asset
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, Number of results wanted. The api return 100 results at a time (default: 100)
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the assets
        """
        
        assets_policy_url = bf_assets_url + bf_assets_policy_url + policy_id
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, assets_policy_url, self.proxies)
        
        #print('[INFO] Function assets_policy, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response

    def assets_policy_info(self, policy_id: str, nb_of_results: int=None, pandas: bool=False) -> Union[pd.DataFrame, list]:
        '''
        Obtain informations about the assets minted under a specific policy ID.

        :param policy_id: Policy ID
        :nb_of_results: Optional, Number of results wanted. The api return 100 results at a time (default: None)
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dict or DataFrame with the informations on each asset under the policy and the list ofbthe asset not found
        '''
        
        assets_informations = []
        
        #print('[INFO] Get the asset names minted under the policy ID: {}'.format(policy_id))
        asset_minted_names = self.assets_policy(policy_id, pandas=True, nb_of_results=nb_of_results)['asset'].tolist()

        #print('[INFO] Get the information about the assets.'.format(policy_id))
        for asset in tqdm(asset_minted_names):
            response = self.specific_asset(asset)
        
            # Add the asset data info to the list of assets
            assets_informations.append(add_onchain_metadata(response))

        #print('[INFO] Function specific_asset, {} API calls.'.format(len(assets_data)))

        return pd.DataFrame.from_dict(assets_informations) if pandas else assets_informations

    def specific_tx(self, txs_hash: str) -> dict: 
        """
        Obtain the content of the requested transaction.
        
        :param txs_hash: Transaction hash
        :return: Dictionary with the info about the content of the transaction
        """
        
        specific_tx_url = self.network + bf_tx_url + txs_hash

        response = query_blockfrost(specific_tx_url, self.api_key, self.proxies)
        
        return response

    def tx_utxos(self, txs_hash: str) -> dict: 
        """
        Return the inputs and UTXOs of the specific transaction.
        
        :param txs_hash: Transaction hash
        :return: Dictionary with the info about the inputs and UTXOs of the specific transaction
        """
        
        specific_tx_utxos_url = self.network + bf_tx_url + txs_hash + bf_tx_utxos_url

        response = query_blockfrost(specific_tx_utxos_url, self.api_key, self.proxies)
        
        return response

    def tx_stake_address_cert(self, txs_hash: str, pandas: bool=False) -> dict: 
        """
        Obtain information about (de)registration of stake addresses within a transaction.
        
        :param txs_hash: Transaction hash
        :return: Dictionary with the info about (de)registration of stake addresses within a transaction
        """
        
        stake_address_certificates_url = self.network + bf_tx_url + txs_hash + bf_stake_address_certificates_url

        response = query_blockfrost(stake_address_certificates_url, self.api_key, self.proxies)
        
        return pd.DataFrame.from_dict(response) if pandas else response

    def tx_delegation_cert(self, txs_hash: str, pandas: bool=False) -> dict: 
        """
        Obtain information about delegation certificates of a specific transaction.
        
        :param txs_hash: Transaction hash
        :return: Dictionary with the info about delegation certificates of a specific transaction
        """
        
        tx_delegation_certificates_url = self.network + bf_tx_url + txs_hash + bf_tx_delegation_certificates_url

        response = query_blockfrost(tx_delegation_certificates_url, self.api_key, self.proxies)
        
        return pd.DataFrame.from_dict(response) if pandas else response

    def tx_withdrawal_url(self, txs_hash: str, pandas: bool=False) -> dict: 
        """
        Obtain information about withdrawals of a specific transaction.
        
        :param txs_hash: Transaction hash
        :return: Dictionary with the info about withdrawals of a specific transaction
        """
        
        tx_withdrawal_url = self.network + bf_tx_url + txs_hash + bf_tx_withdrawal_url

        response = query_blockfrost(tx_withdrawal_url, self.api_key, self.proxies)
        
        return pd.DataFrame.from_dict(response) if pandas else response

    def tx_transaction_mirs(self, txs_hash: str, pandas: bool=False) -> dict: 
        """
        Obtain information about withdrawals of a specific transaction.
        
        :param txs_hash: Transaction hash
        :return: Dictionary with the info about withdrawals of a specific transaction
        """
        
        tx_transaction_mirs = self.network + bf_tx_url + txs_hash + bf_tx_transaction_mirs_url

        response = query_blockfrost(tx_transaction_mirs, self.api_key, self.proxies)
        
        return pd.DataFrame.from_dict(response) if pandas else response

    def tx_stake_pool_update(self, txs_hash: str, pandas: bool=False) -> dict: 
        """
        Obtain information about stake pool registration and update certificates of a specific transaction.
        
        :param txs_hash: Transaction hash
        :return: Dictionary with the info about stake pool registration and update certificates of a specific transaction
        """
        
        tx_stake_pool_update_url = self.network + bf_tx_url + txs_hash + bf_tx_stake_pool_update_url

        response = query_blockfrost(tx_stake_pool_update_url, self.api_key, self.proxies)
        
        return pd.DataFrame.from_dict(response) if pandas else response

    def tx_stake_pool_retirement_cert(self, txs_hash: str, pandas: bool=False) -> dict: 
        """
        Obtain information about stake pool retirements within a specific transaction.
        
        :param txs_hash: Transaction hash
        :return: Dictionary with the info about stake pool retirements within a specific transaction
        """
        
        tx_stake_pool_retirement_cert_url = self.network + bf_tx_url + txs_hash + bf_tx_stake_pool_retirement_cert_url

        response = query_blockfrost(tx_stake_pool_retirement_cert_url , self.api_key, self.proxies)
        
        return pd.DataFrame.from_dict(response) if pandas else response

    def tx_metadata(self, txs_hash: str, pandas: bool=False) -> dict: 
        """
        Obtain the transaction metadata.
        
        :param txs_hash: Transaction hash
        :return: Dictionary with the info about the transaction metadata
        """
        
        tx_metadata_url = self.network + bf_tx_url + txs_hash + bf_tx_metadata_url

        response = query_blockfrost(tx_metadata_url , self.api_key, self.proxies)
        
        return pd.DataFrame.from_dict(response) if pandas else response

    def tx_cbor_metadata(self, txs_hash: str, pandas: bool=False) -> dict: 
        """
        Obtain the transaction metadata in CBOR.
        
        :param txs_hash: Transaction hash
        :return: Dictionary with the info about the transaction metadata in CBOR
        """
        
        tx_cbor_metadata_url = self.network + bf_tx_url + txs_hash + bf_tx_cbor_metadata_url

        response = query_blockfrost(tx_cbor_metadata_url, self.api_key, self.proxies)
        
        return pd.DataFrame.from_dict(response) if pandas else response

    def tx_redeemers(self, txs_hash: str, pandas: bool=False) -> dict: 
        """
        Obtain the transaction redeemers.
        
        :param txs_hash: Transaction hash
        :return: Dictionary with the info about the transaction redeemers.
        """
        
        tx_redeemers_url = self.network + bf_tx_url + txs_hash + bf_tx_redeemers_url

        response = query_blockfrost(tx_redeemers_url, self.api_key, self.proxies)
        
        return pd.DataFrame.from_dict(response) if pandas else response

    def scripts_list(self, data_order: str='asc', nb_of_results: int=100, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        List of scripts.
        
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, Number of results wanted. The api return 100 results at a time (default: 100)
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the scripts hash
        """
        
        scripts_url = bf_assets_url + bf_scripts_url
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, bf_scripts_url, self.proxies)
        
        #print('[INFO] Function script_list, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response

    def specific_script(self, script_hash: str) -> dict: 
        """
        Information about a specific script.
        
        :param script_hash: Script hash
        :return: Dictionary with the info about a specific script.
        """
        
        specific_script_url = self.network + bf_specific_script_url + script_hash

        response = query_blockfrost(specific_script_url, self.api_key, self.proxies)
        
        return response

    def redeem_specific_script(self, script_hash: str, data_order: str='asc', nb_of_results: int=100, pandas: bool=False) -> Union[pd.DataFrame, dict]:
        """
        List of redeemers of a specific script.
        
        :param script_hash: Script hash
        :param data_order: Optional, use 'desc' if you want reverse the data order (default: Ascending)
        :param nb_of_results: Optional, Number of results wanted. The api return 100 results at a time (default: 100)
        :param pandas: Optional, True for return a pandas dataframe (default: False)
        :return: Dictionary or DataFrame of the redeemers of a specific script
        """
        
        redeem_specific_script_url = bf_specific_script_url + script_hash + bf_redeem_specific_script_url
        response, count_api_calls = query_on_several_pages(self.network, self.api_key, data_order, nb_of_results, redeem_specific_script_url, self.proxies)
        
        #print('[INFO] Function redeem_specific_script, {} API calls.'.format(count_api_calls))
        
        return pd.DataFrame.from_dict(response) if pandas else response


    def latest_block(self) -> dict:
        """Get the latest block available to the backends, also known as the tip of the blockchain."""
        url = self.network + bf_blocks_url + bf_blocks_latest_url
        return query_blockfrost(url, self.api_key, self.proxies)

    
    def latest_block_tx(self) -> dict:
        """Get the transactions within the latest block."""
        url = self.network + bf_blocks_url + bf_blocks_latest_url + bf_blocks_tx_url
        return query_blockfrost(url, self.api_key, self.proxies)


    def specific_block(self, block_hash_or_nb: str) -> dict: 
        """
        Get information about a specific script.
        
        :param  block_hash_or_nb: Block hash or block number
        :return: Dictionary with the block informations.
        """
        url = self.network + bf_blocks_url + "/{}".format(block_hash_or_nb)
        return query_blockfrost(url, self.api_key, self.proxies)

    
    def next_blocks(self, block_hash_or_nb: str) -> dict: 
        """
        Get the list of blocks following a specific block.
        
        :param  block_hash_or_nb: Block hash or block number
        :return: List with the information about all the folowing block.
        """
        url = self.network + bf_blocks_url + "/{}".format(block_hash_or_nb) + bf_next_blocks_url
        return query_blockfrost(url, self.api_key, self.proxies)

    def previous_blocks(self, block_hash_or_nb: str) -> dict: 
        """
        Get the list of blocks preceding a specific block.
        
        :param  block_hash_or_nb: Block hash or block number
        :return: List with the information about all the previous block.
        """
        url = self.network + bf_blocks_url + "/{}".format(block_hash_or_nb) + bf_pevious_block_url
        return query_blockfrost(url, self.api_key, self.proxies)

    def specific_block_slot(self, slot_number: int) -> dict: 
        """
        Get the content of a requested block for a specific slot.
        
        :param  slot_number: Slot number
        :return: Dictionary with the information about the block.
        """
        url = self.network + bf_blocks_url + bf_blocks_slot_url + "/{}".format(slot_number)
        return query_blockfrost(url, self.api_key, self.proxies)


    def specific_block_epoch_slot(self, epoch_number: int, slot_number: int) -> dict: 
        """
        Get the content of a requested block for a specific slot in an epoch.
        
        :param  epoch_number: Epoch number
        :param  slot_number: Slot number
        :return: Dictionary with the information about the block.
        """
        url = self.network + bf_blocks_url + bf_blocks_epoch + "/{}".format(epoch_number) + bf_blocks_slot_url + "/{}".format(slot_number)
        return query_blockfrost(url, self.api_key, self.proxies)


    def block_transaction(self, block_hash_or_nb: str) -> dict: 
        """
        Get the transactions within the block.
        
        :param  block_hash_or_nb: Block hash or block number
        :return: List with the transactions hashes.
        """
        url = self.network + bf_blocks_url + "/{}".format(block_hash_or_nb) + bf_blocks_tx_url
        return query_blockfrost(url, self.api_key, self.proxies)

    def block_addresses_tx(self, block_hash_or_nb: str) -> dict: 
        """
        Get a list of addresses affected in the specified block with additional information.
        
        :param  block_hash_or_nb: Block hash or block number
        :return: List with the addresses and transation related.
        """
        url = self.network + bf_blocks_url + "/{}".format(block_hash_or_nb) + bf_blocks_addresses_url
        return query_blockfrost(url, self.api_key, self.proxies)

    


    
      
