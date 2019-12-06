<script>
  import {onMount} from 'svelte'
  let question = ""
  let answer = ""
  let difficulty = 1
  let category = "sports"
  let categories = {}
  let success=false
  let fail=false
  


  onMount(() => {
    categories = getCategories()
  })


  
  let getCategories = async () => {
    try {
      const response = await fetch(`${URL}/categories`)
      const res_json = await response.json()
      categories = await res_json["categories"]
      // console.log(categories)
    } catch (error) {
      console.log(error)
    }
  }

  let submitQuestion = async () => {
    let data={
      "question":question,
      "answer":answer,
      "difficulty":difficulty,
      "category":category
    }
    console.log(data)
    try {
      const response = await fetch(`${URL}/questions`, {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify(data),
      })
      if (!response.ok) {
      alert('Unable to submit question.')
      fail=true
      success=false
      return ;}
      const res_json = await response.json()
      console.log(res_json)
      question=""
      answer=""
      success=true      
      fail=false
    } catch (error) {
      console.log(error)
      fail=true
      success=false
    }

  }
</script>


<style>
.alert {
  height:50px;
}


</style>

<div class="container">
<div class="row">

<div id="add-form" class="col-6" >

  <h2>Add a New Trivia Question</h2>
  <form className="form-view" id="add-question-form" on:submit|preventDefault={()=>submitQuestion()}>

   <div class="form-group">
    <label for="question">
      Question
      <textarea class="form-control" id="question" rows="3" bind:value={question} required></textarea>
    </label>
    </div>

    <div class="form-group">
    <label for="answer">
      Answer
      <input type="text" class="form-control" id="answer" bind:value={answer} required/>
    </label>
    </div>

    <div class="form-group">
    <label for="difficulty">
      Difficulty
      <select id="difficulty" class="form-control" bind:value={difficulty} required>
        <!-- <option disabled class:selected="{selected}">
        select difficulty
        </option> -->
        <option value="1" selected>1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
      </select>
    </label>
    </div>

    <div class="form-group">
    <label for="category">
      Category
      <select class="form-control" id="category"  bind:value={category} required>
        <!-- <option disabled selected="selected">
        select category
        </option> -->
        {#each categories as {type,id} (id)}
			    <option value={type.toLowerCase()}>
				  {type}
			    </option>
		      {/each}
	      </select>
        </label>
      </div>

        <div class="form-group">
          <input type="submit" class="btn btn-primary" value="Submit" />
        </div>
        </form>
      </div>
      {#if success} 
      <div class="alert alert-primary col-6 " role="alert">
        Question created successfully.
      </div>
      {/if}
      {#if fail} 
      <div class="alert alert-danger col-6 " role="alert">
        Creation failed.
      </div>
      {/if}
    </div>
</div>

