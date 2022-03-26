# MINT批量上架Opensea指导教程

该教程将指导如何将NFT通过mint部署到Polygon网络（ETH也可用），批量上架到Opensea

To find out more please visit:

[📺 bilibili](https://space.bilibili.com/1561886967)



## Step1.将Metamask导入Polygon网络

1. [chainlist](https://chainlist.org/ )
2. 点击  connect to Wallet
3. 将Metamask网络切换至Polygon主网（链ID：137）



## Step2.NFT上传IPFS

1.下载，安装IPFS客户端

```url
https://github.com/ipfs/ipfs-desktop/releases
```

选择 [IPFS-Desktop-Setup-0.20.3.exe](https://github.com/ipfs/ipfs-desktop/releases/download/v0.20.3/IPFS-Desktop-Setup-0.20.3.exe)



2.导入NFT

​	将NFT文件夹导入到IPFS客户端上（最好是相同的后缀名整理在一起）



3.准备json文件

​	与NFT相对应，并上传至IPFS



## Step3.部署上链合约

1.到github上面copy合约

```url
https://github.com/JosephGitHubAccount/nft-tools.git
```

mint/nft_chain.sol



2.打开Remix IDE

```sh
https://remix.ethereum.org/
```



3.将合约放到Remix上面，编译 -> 发布

​	发布时，注意选择Inject Web3，会弹出Metamask，选择polygon网络



## Step4.导入Opensea

https://opensea.io/collections



![image-20220326164350905](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20220326164350905.png)

