SELECT [reference], [estimation], [name], [description], [notes], [from],
[to], [advertiserReference], [salesmanReference], [state], [proposedOn], [actionOn], [actionBy], [radio]
FROM SalesPropositions
WHERE [salesmanReference] = :salesmanReference AND [radio] = :radio
ORDER BY [name]
OFFSET :offset ROWS FETCH NEXT :fetch ROWS ONLY