

<script>
    import {onMount} from 'svelte'
    import Question from './Question.svelte'
    import Search from './Search.svelte'
    import Pagination from './Pagination.svelte'


    const questions_per_page=3

    let questions=[]
    let totalQuestions=0
    let categories=[]
    let current_category=null
    let current_category_id=null
    let page=1

    $: maxPage = Math.ceil(totalQuestions / questions_per_page)
    $: pageNumbers = [page-1,page,page+1].filter(x=>x>0 && x<=maxPage);

    // $: console.log(page,pageNumbers,maxPage)

    URL="http://localhost:2800"

    onMount( ()=> {
      getCategories() 
      getQuestions()
      })
       
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

    let getQuestions =async ()=>{
        try {
            current_category=null
            current_category_id=null
            const response=await fetch(`${URL}/questions?page=${page}`)
            if (!response.ok) alert('Unable to load questions. Please try your request again')
            const res_json=await response.json()
            questions= await res_json.questions
            totalQuestions= await res_json.total_questions
            // console.log(current_category,questions,totalQuestions)
        } catch (error){
            console.log(error)    
        }
    }

  let selectPage=(num)=> {
    page=num
    current_category ? getByCategory(current_category_id) : getQuestions()
  }
  
// you should put id !!!
let getByCategory=async id=>{
  try{
    current_category_id=id
    const response=await fetch(`${URL}/categories/${id}/questions?page=${page}`)
    if (!response.ok) alert('Unable to load questions. Please try your request again')
    const res_json=await response.json()
    // console.log(res_json)
    questions= await res_json.questions
    current_category=await res_json.current_category
    current_category_id=await res_json.category_id
    // i didn't pagination on the server side !
    totalQuestions=await res_json.total_questions
    // console.log(current_category,current_category_id,questions,totalQuestions)
  } catch (error){
    console.log(error)
  }
}

let submitSearch =async searchterm =>{
  try {
  const response = await fetch(`${URL}/questions/search`,{
    headers:{
      'Accept':'application/json',
      'Content-Type':'application/json'
    },
    method:'POST',
    body: JSON.stringify({"searchterm": searchterm}),
  })
  if (!response.ok) alert('Unable to load questions. Please try your request again')
  const res_json=await response.json()
  questions= await res_json.questions
  totalQuestions=await questions.length
  // console.log(questions,totalQuestions)
  } catch (error){
    console.log(error)
  }

}

let deleteQuestion=async id=>{
  if(window.confirm('are you sure you want to delete the question?')){
    try {
    const response=await fetch(`${URL}/questions/${id}`,{
      headers:{
      'Accept':'application/json',
      'Content-Type':'application/json'
    },
      method:'DELETE'
    })
    const res_json=await response.json()
    const message=res_json.message
    console.log(message)
  
    } catch (error){
      console.log(error)
    }
  }
  const response = await getQuestions()
  if (!response.ok) alert('Unable to load questions. Please try your request again')
}
</script>

<style>
img {
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

.categories-title{
  cursor: pointer;
}


</style>


<div class="row">
  <div class="col-md-3 col-12">
    <div class="categories-list">
      <h2 on:click={() => {page=1; getQuestions()}} class="text-center my-3 categories-title">Categories</h2>
        <ul>
          {#each categories as {type,id} (id) }
            <li on:click={() =>{page=1; getByCategory(id)}} class="list-group-item list-group-item-warning categories">
              <p>{type}</p>
              <p>
              <img class="category" src={`${type}.svg`.toLowerCase()}  alt="category"/>
              </p>
            </li>
          {/each}          
          <li><Search {submitSearch}/></li>
        </ul>
        <br>
    </div>
  </div>
  <div class="questions-list offset-md-1 col-md-8 col-12" >

    <h2 class="text-center my-3">
    {#if current_category}
      <span>{current_category}</span>
    {/if}
      Questions</h2>

      {#each questions as {answer,question,difficulty,id,category} (id)}
        <Question {question} {id} {answer} {category} {difficulty} {deleteQuestion} {categories}/>
      {/each}          
      <Pagination {selectPage} {maxPage} {page} {pageNumbers}/>
  </div>
</div>
 