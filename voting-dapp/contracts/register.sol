// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract register {
  address[] _usernames;
  uint[] _passwords;

  mapping(address=>bool) _users;

  function signup(address username,uint password) public {
    require(!_users[msg.sender]);

    _usernames.push(username);
    _passwords.push(password);
    _users[msg.sender]=true;
  }

  function login(address username,uint password) public view returns(bool) {
    uint i;

    for(i=0;i<_usernames.length;i++){
      if(_usernames[i]==username && _passwords[i]==password){
        return true;
      }
    }
    return false;
  }
}
