pragma solidity 0.8.18;

contract main {

    uint[] _result;

    function pal(uint a) public {
        uint rev=0; // 121
        uint dummy;
        uint b;
        b=a; // b=123, a=123
        while(a!=0){ // 1!=0
            dummy=a%10; // 1%10 -> 1
            rev=(rev*10)+dummy; // 321
            a=a/10; // 0
        }
        if(rev==b) // 121 == 121
            _result.push(b);
    } 

    function printOutput() public view returns(uint[] memory){
        return _result;
    } 
}
