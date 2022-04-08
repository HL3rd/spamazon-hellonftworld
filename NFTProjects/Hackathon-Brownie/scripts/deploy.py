from brownie import Barter, interface, config
from scripts.helpful_scripts import get_account


accountPublic1 = config["wallets"]["public1"]
accountPublic2 = config["wallets"]["public2"]
account1 = get_account(1)
account2 = get_account(2)
nft_address = '0x3F029AB70b36848e7D9b615FE70de3367dBF8821'
tokenID = 0



    # print(interface.ERC20('0xc778417E063141139Fce010982780140Aa0cD5Ab').balanceOf(accountPublic1))
    # NFT = interface.IERC721('0x958ba3A9cC45A01A5C1D58831E6F6421C8b9640D')
    # print(NFT.balanceOf(accountPublic1))
    # print(NFT.ownerOf(0))



#IERC721().approve(address, tokenID)


def interact():
        swap = Barter[-1]
        weth_addr = '0xc778417E063141139Fce010982780140Aa0cD5Ab'
        weth_token = interface.ERC20(weth_addr)

        buyer = accountPublic1
        seller = accountPublic2

        nft = interface.IERC721(nft_address)

        print("____________________Basic Data___________________________________")
        print('\ncontract address: ',swap.address)
        
        
        #Preliminary Stats:
        seller_address = swap.sellerCollateralNFT(buyer, nft_address, tokenID)
        amount = swap.valueBorrowedOneNFT(buyer, nft_address, tokenID)

        print('\n____________________Stats before transactions____________________')
        print('\nnft owner:        ',nft.ownerOf(tokenID))
        print('amount owed:      ',amount)


        #______________________Collateral Purcase______________________
        #nft.approve(swap.address, tokenID, {"from": account1})
        #swap.collateralizedPurchase(buyer, seller, nft_address, tokenID, 1*10**16, {"from": account1})

        print('total borrowed ETH',swap.totalValueBorrowed(accountPublic1))
        print('ETH owed against one NFT', swap.valueBorrowedOneNFT(accountPublic1, nft_address, tokenID))
    

        #____________________________Repay____________________________
        #weth_token.approve(swap.address, amount, {"from": account1})
        #swap.repay(nft_address, tokenID, amount, {"from": account1})


        #____________________________Trade____________________________
        #nft.setApprovalForAll(swap.address, True, {"from": account1})
        #nft.approve(swap.address, tokenID, {"from": account1})
        #swap.exchangeNFT(buyer, seller, nft_address, tokenID, {"from": account1})
        print('trade executed?',nft.ownerOf(0)  == accountPublic2)

        #____________________________Default____________________________
        swap.handleDefault(accountPublic1, nft_address, tokenID, {"from": account1})



        amount2 = swap.valueBorrowedOneNFT(buyer, nft_address, tokenID)

        print('\n____________________Stats after transactions_____________________')
        print('\nnft owner:        ',nft.ownerOf(tokenID))
        print('amount owed:      ',amount2)
        

def reset():

        nft = interface.IERC721(nft_address)
        nft.safeTransferFrom(accountPublic2, accountPublic1, tokenID, {"from": account2})

def main():
    #swap = Barter.deploy({"from": account1})
    swap = Barter[-1]
    #interact()
    #swap.emergencyExit(nft_address, 0, {"from": account1})

    print('seller:         ',swap.sellerCollateralNFT(accountPublic1, nft_address, tokenID))
    print('borrow quantity:',swap.valueBorrowedOneNFT(accountPublic1, nft_address, tokenID))

    reset()
    nft = interface.IERC721(nft_address)
    #print(NFT.balanceOf(accountPublic1))
    print('owned by acct 1?  ', nft.ownerOf(0)  == accountPublic1)
    print('owned by acct 2?  ', nft.ownerOf(0)  == accountPublic2)
    print('owned by contract?', nft.ownerOf(0)  == swap.address)



