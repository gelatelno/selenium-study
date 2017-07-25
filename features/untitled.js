db.orders.aggregate([
... {$match:{status: ["done", "expired", "executed", "canceled", "in_progress"]}},
... {$group:{_id:"$payment.system", status: "$status",
... count:{$sum:1}}},
... {$lookup: {from:"payment_systems",
... localField:"_id",
... foreignField:"_id", as:"PS"}},
... {$unwind: "$PS"},
... {$project: {count: 1, "PS.name": 1, "PS.type": 1}},
 { $project: {count: 1, info: { $concat: [ "$PS.type", "/", "$PS.name"] } } }])
