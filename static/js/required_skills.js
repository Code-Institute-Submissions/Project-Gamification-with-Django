(function(){

    document.querySelector('#skillInput').addEventListener('keydown', function(e){
        if (e.keyCode != 13){
            return;
        }
        
        e.preventDefault()
        
        
        var skillName = this.value
        this.value = ''
        addNewSkill(skillName)
        updateSkillsString()
   })

    function addNewSkill(name){
        
        document.querySelector('#skillsContainer').insertAdjacentHTML('beforeend',
        `
        <li class="skill">
        <span class="name">${name}</span>
        <span onclick="removeSkill(this)" class="btnRemove bold">X</span>
        </li>`)
    }
    
  
})()


function fetchSkillArray(){
        var skills = []
        
        document.querySelectorAll('.skill').forEach(function(e){
            name = e.querySelector('.name').innerHTML
            if (name == '') return
            skills.push(name)
        })
        
        return skills
        
    }
    
function updateSkillsString(){
    skills = fetchSkillArray()
    document.querySelector('input[name="skillsString"]').value = skills.join(',')
}

function removeSkill(e){
    e.parentElement.remove()
    updateSkillsString()
}