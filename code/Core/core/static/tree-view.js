// originalni kod:  https://observablehq.com/@d3/collapsible-tree
// skripta za generisanje tree view

const treeDiagonal = d3.linkHorizontal().x(d => d.y).y(d => d.x);

const rootNode = nodes[0]; // Get the first node from the nodes list
const treeData = {id: rootNode.id, name: rootNode.name, children: generateTree(0)};

function generateTree(nodeId, visited = []) {
    const children = [];
    visited.push(nodeId); // Mark the current node as visited

    for (let i = 0; i < nodes.length; i++) {
        if (edgeMatrix[nodeId][i] && !visited.includes(i)) {
            const childNode = {id: nodes[i].id, name: nodes[i].name, children: generateTree(i, visited.slice())};
            children.push(childNode);
        }
    }

    return children.length ? children : null; // Return null if there are no children
}

const treeMargin = {top: 10, right: 120, bottom: 10, left: 40};
const treeWidth = 450;
const treeDx = 10;
const treeDy = treeWidth / 6;

const treeLayout = d3.tree().nodeSize([treeDx, treeDy]);

const treeRoot = d3.hierarchy(treeData, d => d.children); // Specify children accessor

treeRoot.x0 = treeDy / 2;
treeRoot.y0 = 0;
treeRoot.descendants().forEach((d, i) => {
    d.index = i; // Assign an index to each node
    d._children = d.children;
    if (d.data.name !== "aaaa") {
        d.children = null;
    }
});

const treeSvg = d3.create("svg")
    .attr("viewBox", [-treeMargin.left, -treeMargin.top, treeWidth, treeDx])
    .style("font", "10px sans-serif")
    .style("user-select", "none");

const treeGLink = treeSvg.append("g")
    .attr("fill", "none")
    .attr("stroke", "#555")
    .attr("stroke-opacity", 0.4)
    .attr("stroke-width", 1.5);

const treeGNode = treeSvg.append("g")
    .attr("cursor", "pointer")
    .attr("pointer-events", "all");

function treeUpdate(source) {
    const duration = d3.event && d3.event.altKey ? 2500 : 250;
    const nodes = treeRoot.descendants().reverse();
    const links = treeRoot.links();

    // Compute the new tree layout.
    treeLayout(treeRoot);

    let left = treeRoot;
    let right = treeRoot;
    treeRoot.eachBefore(node => {
        if (node.x < left.x) left = node;
        if (node.x > right.x) right = node;
    });

    const height = right.x - left.x + treeMargin.top + treeMargin.bottom;

    const transition = treeSvg.transition()
        .duration(duration)
        .attr("viewBox", [-treeMargin.left, left.x - treeMargin.top, treeWidth, height])
        .tween("resize", window.ResizeObserver ? null : () => () => treeSvg.dispatch("toggle"));

    // Update the nodes...
    const node = treeGNode.selectAll("g")
        .data(nodes, d => d.index);

    // Enter any new nodes at the parent's previous position.
    const nodeEnter = node.enter().append("g").attr("class", "tree-node")
        .attr("transform", d => `translate(${source.y0},${source.x0})`)
        .attr("fill-opacity", 0)
        .attr("stroke-opacity", 0)
        .on("click", (event, d) => {
            // Print the ID of the clicked node to the console
            console.log("Clicked node ID:", d.data.id);

            // Remove the red color from all nodes
            d3.selectAll(".tree-node").attr("fill", d => d._children ? "#555" : "#999");

            // Apply the red color to the clicked node
            d3.select(event.currentTarget).attr("fill", "red");

            d.children = d.children ? null : d._children;
            treeUpdate(d);

            // Find the corresponding node in the main-visual
            const targetNodeId = d.data.id;
            const targetNode = d3.selectAll("#visualization .node")
                .filter(node => node.id === targetNodeId);

            // Trigger the click event of the corresponding node in the main-visual
            const clickHandler = targetNode.on("click");
            if (clickHandler) {
                clickHandler(targetNode.node(), targetNode.datum());
            }
        });


    nodeEnter.append("circle")
        .attr("r", 2.5)
        .attr("fill", d => d._children ? "#555" : "#999")
        .attr("stroke-width", 10);

    nodeEnter.append("text")
        .attr("dy", "0.31em")
        .attr("x", d => d._children ? -6 : 6)
        .attr("text-anchor", d => d._children ? "end" : "start")
        .text(d => d.data.name)
        .clone(true).lower()
        .attr("stroke-linejoin", "round")
        .attr("stroke-width", 3)
        .attr("stroke", "white");

    // Transition nodes to their new position.
    const nodeUpdate = node.merge(nodeEnter).transition(transition)
        .attr("transform", d => `translate(${d.y},${d.x})`)
        .attr("fill-opacity", 1)
        .attr("stroke-opacity", 1);

    // Transition exiting nodes to the parent's new position.
    const nodeExit = node.exit().transition(transition).remove()
        .attr("transform", d => `translate(${source.y},${source.x})`)
        .attr("fill-opacity", 0)
        .attr("stroke-opacity", 0);

    // Update the links...
    const link = treeGLink.selectAll("path")
        .data(links, d => d.target.index);

    // Enter any new links at the parent's previous position.
    const linkEnter = link.enter().append("path")
        .attr("d", d => {
            const o = {x: source.x0, y: source.y0};
            return treeDiagonal({source: o, target: o});
        });

    // Transition links to their new position.
    link.merge(linkEnter).transition(transition)
        .attr("d", treeDiagonal);

    // Transition exiting nodes to the parent's new position.
    link.exit().transition(transition).remove()
        .attr("d", d => {
            const o = {x: source.x, y: source.y};
            return treeDiagonal({source: o, target: o});
        });

    // Stash the old positions for transition.
    treeRoot.eachBefore(d => {
        d.x0 = d.x;
        d.y0 = d.y;
    });
}

treeUpdate(treeRoot);

document.querySelector(".tree-view.border-frame").appendChild(treeSvg.node());