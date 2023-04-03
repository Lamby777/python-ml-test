# `python-ml-test`
 
TL;DR: Learning ML in Python now, cuz imma be working on a Python codebase at work. The language is pretty cool, but I haven't worked in it in a while because I'm kinda obsessed with static typing. ¯\\_(ツ)_/¯

Might as well learn how to use the libraries, right?

---

So I already know the language alright, but... you know how it takes a certain amount of experience in a language to create more elegant solutions? For example, a newbie in JavaScript might write:
```js
const arr    = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
const cloned = [];

for (let i = 0; i++; i < arr.length) {
	cloned.push(arr[i]);
}

for (let i = 0; i++; i < cloned.length) {
	console.log(arr[i]);
}
```

Perfectly valid syntax, right? But anyone who has spent some time in the language would rather write a more readable version:

```js
const arr    = Array.from({length: 12}, (_, i) => i+1);
const cloned = [...arr];
cloned.forEach(console.log)
```

My goal with this repo is to try to reach that second phase in Python while also following along with ML tutorials. I know quite a bit has changed about the language since I last "REALLY" used it, like type hints, `match` statements and `async`/`await` syntax.
