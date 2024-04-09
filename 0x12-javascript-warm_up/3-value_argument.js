#!/usr/bin/node
const firstarg = process.argv[1];
if(firstarg === 0){
    console.log('No argument');
}else{
    console.log(firstarg);
}
