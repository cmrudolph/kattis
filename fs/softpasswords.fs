// NAME : Soft Passwords
// URL  : https://open.kattis.com/problems/softpasswords
// =============================================================================
// Problem where a given input string needs to be compared with N other derived
// strings to see whether any of them match. All possible valid matches are
// derived so a simple "list contains" search can be done
// =============================================================================

open System

let invertCase c =
    let isUpper = Char.IsUpper(c)
    match isUpper with
        | true -> System.Char.ToLower(c)
        | false -> System.Char.ToUpper(c)

let generateMatches p =
    let appended = [0..9] |> List.map (function x -> p + (string x))
    let prepended = [0..9] |> List.map (function x -> (string x) + p)
    let inverted = Seq.toList p |> List.map invertCase |> List.toArray |> System.String
    [p] @ [inverted] @ appended @ prepended

let solve s p =
    let valid = generateMatches p |> List.exists ((=) s)
    match valid with
        | true -> "Yes"
        | false -> "No"

[<EntryPoint>]
let main argv =
    let s = Console.ReadLine()
    let p = Console.ReadLine()
    solve s p |> fun result -> Console.WriteLine(result)
    0
