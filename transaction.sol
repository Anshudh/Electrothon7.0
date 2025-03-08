// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract UserAccount {
    struct User {
        string name;
        address userAddress;
       
    }

    mapping(address => User) private users;
    event UserCreated(address indexed userAddress, string name);
    event HashSent(address indexed sender, address indexed recipient);

    function createUser(string memory name) public {
        require(bytes(name).length > 0, "Name cannot be empty");
        require(users[msg.sender].userAddress == address(0), "User already exists");

        users[msg.sender] = User({
            name: name,
            userAddress: msg.sender
            
        });

        emit UserCreated(msg.sender, name);
    }

    function sendHash(address recipient) public {
        require(users[msg.sender].userAddress != address(0), "Sender does not exist");
        require(users[recipient].userAddress != address(0), "Recipient does not exist");
        

        

        emit HashSent(msg.sender, recipient);
    }

    function getUser(address userAddress) public view returns (string memory name) {
        require(users[userAddress].userAddress != address(0), "User does not exist");

        User memory user = users[userAddress];
        return (user.name);
    }
}
