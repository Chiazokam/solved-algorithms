const votes = ['Glenn', 'Emily', 'Faisal', 'Emily', 'Glenn'];


function count(name, array) {
  let nameCount = 0;
  array.forEach(function(item) {
  if (item === name) {
    nameCount = nameCount + 1;
  }
 })
 return nameCount
}




function voteWinner(votes)
{
  let highestVote = votes[0];
  let highestVoteCount = 0;
  
  const votesSet = new Set(votes);
  const votesArray = Array.from(votesSet);

  votesArray.forEach(function(vote) {
   const voteCount = count(vote, votes);
   if (voteCount > highestVoteCount) {
     highestVoteCount = voteCount;
     highestVote = vote;
   }
   if (voteCount === highestVoteCount) {
     if ( vote > highestVote) {
       highestVote = vote;
     }
   }  
 })
  return highestVote;
}

