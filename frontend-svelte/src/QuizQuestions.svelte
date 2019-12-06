<script>
export let questions
export let guess=""
export let evaluateAnswer
export let currentQuestionIndex
export let showAnswer
export let nextQuestion



</script>

<style>


.Question-holder {
  padding: 10px 20px;
  border: 2px rgb(2, 2, 51) solid;
  border-radius: 10px;
  text-align: left;
  margin: 7px;
  background-color: rgb(162, 224, 120);
}

.Question-status {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}

.Question {
  font-size: 21px;
  width: 100%;
}

form{
    width:50%;
}

.visible{
  display: block;
}
.hidden{
  display: none;
}


</style>



    {#each questions as {question,answer,id},index (id)}
      <div class={index===currentQuestionIndex? "visible":"hidden"}>
      <div class="Question-holder">
        <div class="Question-status">
          <div class="Question">
            {question}            
          </div>
        </div>
          <form on:submit|preventDefault={()=>evaluateAnswer(guess,answer)}>
           <div class="form-group">
            <label for="yourguess">Your Answer</label>
            <input type="text" bind:value={guess} class="form-control" id="yourguess" >        
            </div>
          </form> 
      </div>
      {#if showAnswer}
      <button class="btn btn-warning py-3">The answer is : {answer}</button>
      <button on:click={nextQuestion} class="btn btn-danger py-3">Next Question</button>
      {/if}
    </div>
    {/each}