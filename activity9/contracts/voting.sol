// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract voting {
  uint[3] _votes; // 3 contenstants
  
  mapping(address=>bool) _voters;

  constructor() public {
    _votes[0]=0;
    _votes[1]=0;
    _votes[2]=0;
  }

  function castVote(uint id) public {
    require(!_voters[msg.sender]);
    if(id==0)
      _votes[0]+=1;
    else if(id==1)
      _votes[1]+=1;
    else if(id==2)
      _votes[2]+=1;
    
    _voters[msg.sender]=true;
  }

  function displayVotes() public view returns(uint[3] memory){
    return(_votes);
  }
}
