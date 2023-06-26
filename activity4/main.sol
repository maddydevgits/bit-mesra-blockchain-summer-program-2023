pragma solidity 0.8.18;

contract main {

    string a;

    function insertName(string memory b) public{
        a=b;
    }

    function printName() public view returns(string memory){
        return(a);
    }
}
