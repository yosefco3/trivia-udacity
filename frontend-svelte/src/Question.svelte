
<script>
export let question
export let id
export let answer
export let category
export let categories
export let difficulty
export let deleteQuestion

let visibleAnswer = false

let handleAnswer=()=>visibleAnswer=!visibleAnswer

let find_category_by_id=id=>{
 let category_obj=categories.find(x=>x.id===id)
 return category_obj.type.toLowerCase()
}

$: category_name= find_category_by_id(category)
</script>

<style>

img{
  width:30px;
}

img.delete{
  cursor: pointer;
}


.Question-holder {
  padding: 10px 20px;
  border: 2px rgb(2, 2, 51) solid;
  border-radius: 10px;
  text-align: left;
  margin: 7px;
  background-color: rgb(218, 248, 240);
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


</style>


<div class="Question-holder">
    <div class="Question">{question}
        <div class="Question-status">
            <img class="category" src={`${category_name}.svg`} alt="category svg"/>
            <small class="difficulty">Difficulty: {difficulty}</small>
            <img src="delete.png" class="delete" on:click={()=>deleteQuestion(id)} alt="delete img"/>        
            {#if visibleAnswer}
              <div class="btn btn-success" on:click={handleAnswer}>{answer}</div>
            {:else}
              <div class="btn btn-info" on:click={handleAnswer} >Show Answer</div>
            {/if}
        </div>
    </div>
</div>

