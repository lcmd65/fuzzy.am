## Documentation
### Requirement
* Python 3.11
* fuzz

### Description
Python script, Fuzz Attributes Matching Al( Levenshtein distance), for finding metadata with attributes in data lake 

### Fuzzy Attributes Matching
#### Fuzzy Logic and Boolean logic difference
![image](https://github.com/DatMinhLeChon/fuzz.am/assets/93373784/23db81c1-0ac6-4883-8147-89124a10e8f5)

#### Fuzzy Matching( base ontology matching)
State of the art of database and module lean management, matching
![image](https://github.com/DatMinhLeChon/fuzz.am/assets/93373784/f71ebccc-bbf2-49bc-a4d3-33a91cff2cb4)

#### Algorithm
    [1]	FUNCTION traverseTreeMatching(tree, depth, machine_param[], score_standard)
    [2]		IF tree IS NULL THEN
    [3]			FOREACH meta in machine_param
    [4]				IF FUZZ(tree, meta) >= score_standard THEN
    [5]					RETURN Map<tree,meta>
    [6]				ELSE DO
    [7]					FOREACH rule IN rule_container
    [8]						IF rule(tree, meta) THEN
    [9]							RETURN Map<tree, meta>
    [10]							BREAK
    [11]					END_IF
    [12]					END_FOREACH
    [13]				END_IF
    [14]			END_FOREACH
    [15]		ELSE DO
    [16]			FOREACH child IN tree.Children
    [17]				traverseTree(child, depth + 1)
    [18]			END_FOREACH
    [19]		END_IF

