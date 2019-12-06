<script>
import {onMount} from 'svelte'
import find_category_by_id from './Question.svelte'
import QuizQuestions from './QuizQuestions.svelte'

const questionsPerPlay = 5; 


let numCorrect= 0

let guess=''
let categories=''
let quiz_category=null
let quiz_category_id=null
let questions=[]
let totalQuestions=0
let preGame=true
let currentQuestionIndex=0
let gameOver=false
let showAnswer=false



URL="http://localhost:2800"

onMount(()=>{
  getCategories()
  }
)


let getCategories =async ()=>{
  try {
    const response=await fetch(`${URL}/categories`)
    const res_json=await response.json()
    categories=await res_json["categories"]
    // console.log(categories)
  } catch (error) {
    console.log(error)
  }
} 

let selectCategory = (id)=>{
  current_category_id=id
  current_category=find_category_by_id(id)
}

let getQuizQuestions=async (category)=>{
  try{
    preGame=false
    const response = await fetch(`${URL}/quizzes`,{
      headers:{
        'Accept':'application/json',
        'Content-Type':'application/json'
      },
      method:'POST',
      body: JSON.stringify({"category": category}),
    })
    if (!response.ok) alert('Unable to load questions. Please try your request again')
    const res_json=await response.json()
    // console.log(res_json)
    questions= await res_json.questions
    totalQuestions=await questions.length
    console.log(questions,totalQuestions)
    
  } catch (error){
    console.log(error)
  }

}


let evaluateAnswer = (guess,answer) => {
    const formatGuess = guess.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()\s]/g,"").toLowerCase()
    const answerArray = answer.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g,"").toLowerCase().split(" ")
    answerArray.includes(formatGuess) ? numCorrect++ :""
    guess=""
    showAnswer=true

    // console.log(currentQuestionIndex,totalQuestions)
  }

  let newGame=()=>{
    numCorrect= 0
    guess=''
    quiz_category=null
    quiz_category_id=null
    questions=[]
    totalQuestions=0
    preGame=true
    currentQuestionIndex=0
    gameOver=false
    showAnswer=false
  }

  let nextQuestion=()=>{
    showAnswer=false
    guess=""
    currentQuestionIndex++
    totalQuestions===currentQuestionIndex ? gameOver=true : ""
  }


</script>


<style>

img{
  width:30px;
}


ul{
  list-style-type: none;
}

.categories {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  cursor: pointer;
}

</style>



<div class="container">
  <h1>Trivia Game</h1>
  {#if preGame}
  <div class="row">
    <div class="col-6">
        <h2>Lets choose category :</h2>
        <ul>
            <li 
            class="list-group-item list-group-item-info categories text-danger"
                on:click={()=>getQuizQuestions(null)}>all categories
             <img class="category" src="all.png"  alt="category"/>
            </li>
          {#each categories as {type,id} (id) }
            <li 
                class="list-group-item list-group-item-info categories text-danger"
                on:click={()=>getQuizQuestions(id)}>
              <p>{type}</p>
              <p>
              <img class="category" src={`${type}.svg`.toLowerCase()}  alt="category"/>
              </p>
            </li>
          {/each}         
        </ul>
    </div>    
  </div>
  {:else}
  <div class="row">
    <div class="col-12">
    {#if gameOver}
      <h3>you got {numCorrect} from {totalQuestions} !</h3>
      <button on:click={newGame} class="btn btn-success">New Game ?</button>
    {/if}
      <QuizQuestions {questions} {guess} {evaluateAnswer} {currentQuestionIndex} {showAnswer} {nextQuestion}/>
    </div>    
  </div>
  {/if }
</div>





