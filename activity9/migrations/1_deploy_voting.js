const voting=artifacts.require('voting');

module.exports=function(deployer){
    deployer.deploy(voting);
}