import styled from "styled-components"

const Container = styled.div`

`;

interface Props {
    title: string,
}

const Title = ({ title }: Props) => (
    <Container>
        <h4>{title}</h4>
        <hr />
    </Container>
);

export default Title;
