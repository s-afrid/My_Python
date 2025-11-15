const submit = document.getElementById("submit")

async function send() {
    submit.addEventListener("click", async (e)=>{
        let title = document.getElementById("title").value
        let desc = document.getElementById("desc").value
        let imp = document.getElementById("important").checked
        let data = {
            title: title,
            desc: desc,
            important: imp
        }

        const req = await fetch('/note', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
        const res = await req.json()
        console.log(res)
    })
}

async function main() {
    send()
}
main()